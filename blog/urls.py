from django.urls import path

from blog.apps import BlogConfig
from blog.views import ArticleListAPIView, ArticleCreateAPIView, CommentViewSet
from rest_framework.routers import DefaultRouter

app_name = BlogConfig.name


router = DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', ArticleListAPIView.as_view(), name='article_list'),
    path('create/', ArticleCreateAPIView.as_view(), name='article_create'),
]
