from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from config import settings
from .models import Article


class ArticleListView(ListView):
    model = Article
    paginate_by = 16

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_published=True).order_by('-created_at')
        return queryset


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()

        if self.object.view_counter == 100:
            self.send_email()

        return self.object

    def send_email(self):
        subject = 'Поздравляем! Статья набрала 100 просмотров.'
        message = (f'Ваша статья "{self.object.title}" набрала 100 просмотров. '
                   f'Сообщество Pure life поздравляет Вас с достижением!')
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
            fail_silently=False,
        )


class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'text', 'photo', 'is_published']
    success_url = reverse_lazy('blog:article_list')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'text', 'photo', 'is_published']
    success_url = reverse_lazy('blog:article_list')

    def get_success_url(self):
        return reverse('blog:article_detail', args=[self.kwargs.get('pk')])


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:article_list')
