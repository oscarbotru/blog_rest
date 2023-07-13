from rest_framework import serializers

from blog.models import Article, Comment, Like
from blog.validators import RudeWordValidator


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    comment = serializers.CharField(validators=[RudeWordValidator])

    class Meta:
        model = Comment
        fields = ['id', 'comment', 'likes']

    def get_likes(self, instance):
        return instance.like_set.all().count()


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['comment', 'article']


class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True, source='comment_set')
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'body', 'comments', 'likes']

    def get_likes(self, instance):
        return instance.like_set.all().count()
