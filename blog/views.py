from rest_framework import generics, viewsets

from blog.models import Article, Comment
from blog.serializers import ArticleSerializer, CommentSerializer


class ArticleListAPIView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleCreateAPIView(generics.CreateAPIView):
    serializer_class = ArticleSerializer


class ArticleUpdateAPIView(generics.UpdateAPIView):
    model = Comment


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.query_params.get('pk'):
            queryset = queryset.filter(article_id=int(self.request.query_params.get('pk')))

        return queryset
