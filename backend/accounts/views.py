from django.contrib.auth import get_user_model, authenticate
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from google.oauth2 import id_token
from google.auth.transport import requests
from django.conf import settings
import logging

from .serializers import UserSerializer, UserRegistrationSerializer

User = get_user_model()
logger = logging.getLogger(__name__)


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user': UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        if email is None or password is None:
            return Response({'error': 'Please provide both email and password'},
                          status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                token, _ = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'user': UserSerializer(user).data
                })
            else:
                return Response({'error': 'Invalid credentials'},
                              status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({'error': 'Invalid credentials'},
                          status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)


class UserDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoogleAuthView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        try:
            token_id = request.data.get('token_id')
            if not token_id:
                logger.error("No token provided in request")
                return Response({'error': 'No token provided'}, status=status.HTTP_400_BAD_REQUEST)
            
            logger.info("Received Google token for verification")
            logger.info("Using client ID: %s", settings.GOOGLE_OAUTH2_CLIENT_ID)
            
            # Verify the token
            try:
                idinfo = id_token.verify_oauth2_token(
                    token_id, 
                    requests.Request(), 
                    settings.GOOGLE_OAUTH2_CLIENT_ID
                )
                logger.info("Token verified successfully")
            except ValueError as e:
                logger.error("Token verification failed: %s", str(e))
                return Response({'error': f'Token verification failed: {str(e)}'}, 
                              status=status.HTTP_400_BAD_REQUEST)
            
            # Get user info from the token
            email = idinfo['email']
            first_name = idinfo.get('given_name', '')
            last_name = idinfo.get('family_name', '')
            logger.info("User info retrieved from token - Email: %s", email)
            
            # Get or create user
            try:
                user = User.objects.get(email=email)
                logger.info("Existing user found: %s", email)
            except User.DoesNotExist:
                # Create new user
                username = email.split('@')[0]
                base_username = username
                counter = 1
                
                # Ensure unique username
                while User.objects.filter(username=username).exists():
                    username = f"{base_username}{counter}"
                    counter += 1
                
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                )
                logger.info("New user created: %s", email)
            
            # Generate token
            token, _ = Token.objects.get_or_create(user=user)
            logger.info("Authentication token generated for user: %s", email)
            
            return Response({
                'token': token.key,
                'user': UserSerializer(user).data
            })
            
        except ValueError as e:
            logger.error("ValueError in Google auth: %s", str(e))
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error("Unexpected error in Google auth: %s", str(e), exc_info=True)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 