from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib import messages
from catalog.models import Contact, Product
from .forms import ProductForm


class ProductListView(ListView):
    model = Product
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')

        list_products = queryset[:5]
        for product in list_products:
            print(f'{product.name} - {product.created_at}')

        return list_products


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    login_url = reverse_lazy('users:login')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ContactsView(TemplateView):
    template_name = 'catalog/contact_form.html'

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.POST.get('name'),
            'phone': request.POST.get('phone'),
            'message': request.POST.get('message'),
        }
        Contact.objects.create(name=data.get('name'), phone=data.get('phone'), message=data.get('message'))
        print(f"Пользователь отправил данные:\nname: {data.get('name')}, phone: {data.get('phone')}, message: {data.get('message')}")
        messages.success(request, 'Ваше сообщение успешно отправлено!')
        return super().get(request, *args, **kwargs)
