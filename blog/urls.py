from django.urls import path

from blog.apps import BlogConfig
from blog.views import ArticleListAPIView, ArticleCreateAPIView, CommentViewSet, ArticleUpdateAPIView, \
    LikeCreateAPIView, ArticleDestroyAPIVIew
from rest_framework.routers import DefaultRouter

app_name = BlogConfig.name


router = DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    # articles
    path('', ArticleListAPIView.as_view(), name='article_list'),
    path('create/', ArticleCreateAPIView.as_view(), name='article_create'),
    path('update/<int:pk>/', ArticleUpdateAPIView.as_view(), name='article_update'),
    path('update/<int:pk>/', ArticleUpdateAPIView.as_view(), name='article_update'),
    path('delete/<int:pk>/', ArticleDestroyAPIVIew.as_view(), name='article_delete'),
    # likes
    path('like/', LikeCreateAPIView.as_view(), name='like'),
] + router.urls
