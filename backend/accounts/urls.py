from django.urls import path
from .views import RegisterView, LoginView, UserDetailView, LogoutView, GoogleAuthView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
    path('google/', GoogleAuthView.as_view(), name='google-auth'),
]