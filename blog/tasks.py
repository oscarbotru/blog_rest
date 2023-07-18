import datetime

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from blog.models import Like


@shared_task
def send_moderator_email():
    send_mail(
        subject='Новый комментарий',
        message='В блоге появился новый комментарий, необходимо провести ревью',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_MODERATOR]
    )


@shared_task
def send_moderator_likes_count():
    likes_count = Like.objects.all().count()
    now = datetime.datetime.now()
    send_mail(
        subject='Количество лайков',
        message=f'На {now} количество лайков: {likes_count}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_MODERATOR]
    )
