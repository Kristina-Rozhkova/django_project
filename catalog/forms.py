from django.core.exceptions import ValidationError
from django.core.validators import validate_image_file_extension
from django.db.models import BooleanField
from django.forms import ModelForm
from .models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    unallowed = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        exclude = ('created_at', 'upload_at', 'publication_status', 'owner')

    def clean_name(self):
        name = self.cleaned_data.get('name').lower()
        if name in self.unallowed:
            raise ValidationError(f'Нельзя называть продукт словом "{name}".')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description').lower()
        for word in self.unallowed:
            if word in description:
                raise ValidationError(f'Исключите слово "{word}" из описания продукта. Это запрещенное слово.')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            max_size = 5 * 1024 * 1024
            if image.size > max_size:
                raise ValidationError('Максимальный размер изображения 5 МБ')
        return image


class ProductModeratorForm(ProductForm):
    class Meta:
        model = Product
        fields = ('publication_status',)
