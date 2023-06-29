from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Статья')

    is_published = models.BooleanField(default=True, verbose_name='опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='статья')
    comment = models.CharField(max_length=250, verbose_name='комментарий')

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'Комментарий #{self.pk} к статье {self.article}'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'


class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='статья')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='комментарий')

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'лайк'
        verbose_name_plural = 'лайки'
