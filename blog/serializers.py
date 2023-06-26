from rest_framework import serializers

from blog.models import Article, Comment, Like


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Article
        fields = ['title', 'body', 'comments_count', 'likes']

    def get_comments_count(self, instance):
        return instance.comment_set.all().count()

    def get_likes(self, instance):
        return instance.like_set.all().count()


class CommentSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = ['comment', 'article', 'likes']

    def get_likes(self, instance):
        return instance.like_set.all().count()
