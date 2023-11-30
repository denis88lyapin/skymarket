from django.conf import settings
from django.db import models


NULLABLE = {
    'blank': True,
    'null': True
}


class Ad(models.Model):
    title = models.CharField(max_length=200, verbose_name='название товара')
    price = models.PositiveIntegerField(verbose_name='цена товара', **NULLABLE)
    description = models.TextField(verbose_name='описание товара', **NULLABLE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')
    image = models.ImageField(upload_to='ads/images', verbose_name='изображение товара', **NULLABLE)

    def __str__(self):
        return f'{self.title} - {self.price}'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']


class Comment(models.Model):
    text = models.TextField(verbose_name='текст отзыва')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='автор', **NULLABLE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='объявление')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата и время')

    def __str__(self):
        return f'{self.author} - {self.text}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
