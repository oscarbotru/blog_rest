from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_moderator_email():
    send_mail(
        subject='Новый комментарий',
        message='В блоге появился новый комментарий, необходимо провести ревью',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_MODERATOR]
    )
