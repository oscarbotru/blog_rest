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

    def test_create_article(self):
        data = {
            'title': 'new test',
            'body': 'new test',
        }

        response = self.client.post(
            reverse('blog:article_create'),
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            2,
            Article.objects.all().count()
        )

    def test_update_article(self):
        data = {
            'title': 'update test',
            'body': 'update test',
        }

        response = self.client.post(
            reverse('blog:article_update', args=[self.article.pk]),
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            self.article.title,
            data['title']
        )
