from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_medical_report_email(user, patient_email, patient_name, report_file, format_type):
    """Send medical report email to patient"""
    subject = 'Votre Rapport Médical'
    
    html_message = render_to_string('email/medical_report_email.html', {
        'patient_name': patient_name,
        'doctor_name': user.username,
        'format': format_type.upper()
    })
    plain_message = strip_tags(html_message)
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [patient_email]
    
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=from_email,
        to=recipient_list
    )
    email.content_subtype = "html"
    email.attach(f'rapport_medical.{format_type}', report_file, f'application/{format_type}')
    email.send()
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(user):
    """Send email confirmation to user"""
    subject = 'Confirmation de votre compte'
    confirmation_url = f"{settings.FRONTEND_URL}/verify-email/{user.email_verification_token}"
    
    html_message = render_to_string('email/confirmation_email.html', {
        'user': user,
        'confirmation_url': confirmation_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )

def send_password_reset_email(user):
    """Send password reset email to user"""
    subject = 'Réinitialisation de votre mot de passe'
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{user.password_reset_token}"
    
    html_message = render_to_string('email/reset_password_email.html', {
        'user': user,
        'reset_url': reset_url,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        html_message=html_message,
    )
