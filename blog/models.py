from django.db import models

class Article(models.Model):
    title = models.CharField (
        max_length=150,
        verbose_name='Заголовок',
        help_text='Введите заголовок статьи'
    )
    text = models.TextField(
        verbose_name='Содержание',
        help_text='Напишите статью'
    )
    photo = models.ImageField(
        verbose_name='Фотография',
        help_text='Загрузите фото',
        upload_to='blog/media',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Опубликовать'
    )
    view_counter = models.PositiveIntegerField(
        verbose_name='Счетчик просмотров',
        help_text='Загрузите количество просмотров',
        default=0
    )

    def __str__(self):
        return f'Статья "{self.title}", статус публикации: {self.is_published}, просмотрена: {self.view_counter} раз.'

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
        ordering = ["title",]
