from django.urls import path

from blog.apps import BlogConfig
from blog.views import ArticleListAPIView, ArticleCreateAPIView

app_name = BlogConfig.name


urlpatterns = [
    path('', ArticleListAPIView.as_view(), name='article_list'),
    path('create/', ArticleCreateAPIView.as_view(), name='article_create'),
]
