from django.shortcuts import get_object_or_404
from catalog.models import Category, Product
from config.settings import CACHE_ENABLED
from django.core.cache import cache


def get_products_in_category(queryset, category_id):
    """Выводит список продуктов из заданной категории, если такая имеется в БД. Иначе выводит ошибку."""
    category = get_object_or_404(Category, id=category_id)
    queryset = queryset.filter(category=category)
    return queryset


def get_products_from_cache():
    """Получает данные по продуктам из кэша. Если кэш пуст, получает данные из БД."""
    if not CACHE_ENABLED:
        return Product.objects.all().order_by('-created_at')
    key = 'product_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all().order_by('-created_at')
    cache.set(key, products)
    return products
