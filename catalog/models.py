from django.core.validators import FileExtensionValidator
from django.db import models

from users.models import User


class Product(models.Model):
    PUBLISHED = 'published'
    UNPUBLISHED = 'unpublished'

    PUBLICATION_STATUS_CHOICES = [
        (PUBLISHED, 'Опубликовать'),
        (UNPUBLISHED, 'На рассмотрении')
    ]

    name = models.CharField(
        max_length=100,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание продукта",
        null=True,
        blank=True,
    )
    image = models.ImageField(
        verbose_name="Изображение",
        help_text="Загрузите изображение",
        upload_to="catalog/media",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(
            allowed_extensions=['jpeg', 'png'],
            message='Допустимы только файлы в формате JPEG или PNG'
        )]
    )
    category = models.ForeignKey(
        "Category",
        verbose_name="Категория",
        help_text="Выберите категорию",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.FloatField(
        verbose_name="Цена за покупку", help_text="Введите цену за покупку продукта"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Укажите дату создания"
    )
    upload_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата последнего изменения",
        help_text="Укажите дату последнего изменения",
    )
    publication_status = models.CharField(
        max_length=15,
        choices=PUBLICATION_STATUS_CHOICES,
        default=UNPUBLISHED,
        verbose_name='Статус публикации'
    )
    owner = models.ForeignKey(
        User,
        verbose_name='владелец',
        blank=True,
        null=True,
        help_text='Укажите владельца',
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f'{self.name} относится к категории "{self.category}". Цена за единицу - {self.price}'

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["category", "name"]
        permissions = [
            ('can_unpublish_product', 'Can unpublish product')
        ]


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Введите категорию товара",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя', help_text='Введите имя')
    phone = models.CharField(max_length=30, verbose_name='Телефон', help_text='Введите номер телефона')
    message = models.TextField(verbose_name='Сообщение', help_text='Введите дополнительную информацию', blank=
    True, null=True)

    def __str__(self):
        return (f'Контактные данные:\n'
                f'Имя: {self.name}\n'
                f'Телефон: {self.phone}')

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        ordering = ['name', ]
