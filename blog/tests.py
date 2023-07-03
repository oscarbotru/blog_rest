import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from blog.models import Article


class BlogTestCase(APITestCase):

    def setUp(self) -> None:
        self.article = Article.objects.create(
            title='test',
            body='test'
        )

    def test_getting_article_list(self):
        response = self.client.get(
            reverse('blog:article_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            json.loads(response.body),
            [
                {
                    'id': self.article.id,
                    'title': self.article.title,
                    'body': self.article.body,
                    'comments': [],
                    'likes': 0
                }
            ]
        )
