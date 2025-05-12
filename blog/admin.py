from django.contrib import admin
from blog.models import Article


@admin.register(Article)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published')
    list_filter = ('created_at','title', 'view_counter')
    search_fields = ('title', 'text')
