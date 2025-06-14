from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email):
    send_mail(
        subject='Welcome to the Platform',
        message='Thanks for registering!',
        from_email='noreply@example.com',
        recipient_list=[email],
        fail_silently=False
    )
