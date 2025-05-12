from django.urls import path
from blog.apps import BlogConfig
from .views import ArticleListView, ArticleCreateView, ArticleDeleteView, ArticleDetailView, ArticleUpdateView


app_name = BlogConfig.name

urlpatterns = [
    path('article_list/', ArticleListView.as_view(), name='article_list'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>/detail/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete')
]
