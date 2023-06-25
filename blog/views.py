from rest_framework import generics
from rest_framework.generics import CreateAPIView

from blog.models import Article
from blog.serializers import ArticleSerializer


class ArticleListAPIView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleCreateAPIView(CreateAPIView):
    serializer_class = ArticleSerializer
