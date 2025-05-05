from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from catalog.models import Contact, Product, Category
import datetime
from django.core.paginator import Paginator


def home(request):
    last_products = Product.objects.all().order_by('-created_at')[:5]

    # определение количества товаров на странице
    paginator = Paginator(last_products, 4)

    page_number = request.GET.get('page')
    # создание объекта страницы с товарами для текущего номера страницы
    page_obj = paginator.get_page(page_number)

    # вывод в консоль последних 5 добавленных продуктов
    print('Последние 5 продуктов:')
    for product in last_products:
        print(f'{product.name} - {product.created_at}')

    return render(request, 'catalog/home.html', {'page_obj': page_obj, 'paginator': paginator})


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Пользователь отправил данные: name: {name}, phone: {phone_number}, message: {message}")
        Contact.objects.create(name=name, phone=phone_number, message=message)
        return HttpResponse('Данные отправлены!')
    return render(request, 'catalog/contacts.html')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context)


def add_new_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        category = request.POST.get('category')
        if category:
            category_id = Category.objects.get(id=category)
        price = request.POST.get('price')

        Product.objects.create(
            name=name,
            description=description,
            category=category_id if category else None,
            price=price,
            image=image,
            created_at=datetime.date.today(),
            upload_at=datetime.date.today()
        )
        return redirect('catalog:home')
    categories = Category.objects.all()
    return render(request, 'catalog/add_new_product.html', {'categories': categories})