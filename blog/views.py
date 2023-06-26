from rest_framework import generics, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from blog.models import Article, Comment
from blog.serializers import ArticleSerializer, CommentSerializer, LikeSerializer, CommentCreateSerializer


class ArticleListAPIView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleCreateAPIView(CreateAPIView):
    serializer_class = ArticleSerializer


class ArticleUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ArticleSerializer


class ArticleDestroyAPIVIew(generics.DestroyAPIView):
    queryset = Article.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.query_params.get('pk'):
            queryset = queryset.filter(article_id=int(self.request.query_params.get('pk')))

        return queryset

    def create(self, request, *args, **kwargs):
        self.serializer_class = CommentSerializer
        return super().create(request, *args, **kwargs)


class LikeCreateAPIView(generics.CreateAPIView):
    serializer_class = LikeSerializer
