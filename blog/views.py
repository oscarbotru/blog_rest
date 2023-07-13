import requests
from rest_framework import generics, viewsets, status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Article, Comment
from blog.paginators import MyPagination
from blog.permissions import AuthorOrManager
from blog.serializers import ArticleSerializer, CommentSerializer, LikeSerializer, CommentCreateSerializer


class ArticleListAPIView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.filter(is_published=True)
    pagination_class = MyPagination


class ArticleCreateAPIView(CreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_article = serializer.save()
        new_article.author = self.request.user
        new_article.save()


class ArticleUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [AuthorOrManager]
    queryset = Article.objects.all()


class ArticleDestroyAPIVIew(generics.DestroyAPIView):
    queryset = Article.objects.all()
    permission_classes = [AuthorOrManager]

    def perform_destroy(self, instance):
        instance.is_published = False
        instance.save()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.query_params.get('pk'):
            queryset = queryset.filter(article_id=int(self.request.query_params.get('pk')))

        return queryset

    def create(self, request, *args, **kwargs):
        self.serializer_class = CommentCreateSerializer
        new_comment = super().create(request, *args, **kwargs)
        new_comment.author = self.request.user
        new_comment.save()
        return new_comment


class LikeCreateAPIView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]


class WeatherAPIView(APIView):

    def get(self, *args, **kwargs):
        return Response(
            data={
                'weather': requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true')
            },
            status=status.HTTP_200_OK
        )
