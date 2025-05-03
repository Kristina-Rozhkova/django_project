from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Contact, Product


def home(request):
    last_products = Product.objects.all().order_by('-created_at')[:5]

    # вывод в консоль последних 5 добавленных продуктов
    print('Последние 5 продуктов:')
    for product in last_products:
        print(f'{product.name} - {product.created_at}')

    return render(request, 'catalog/home.html', {'last_products': last_products})


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Пользователь отправил данные: name: {name}, phone: {phone_number}, message: {message}")
        Contact.objects.create(name=name, phone=phone_number, message=message)
        return HttpResponse('Данные отправлены!')
    return render(request, 'catalog/contacts.html')
