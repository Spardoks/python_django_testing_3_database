from django.shortcuts import redirect, render

from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_method = request.GET.get('sort', None)
    if sort_method == 'name':
        phone_objects = Phone.objects.all().order_by('name')
    elif sort_method == 'min_price':
        phone_objects = Phone.objects.all().order_by('price')
    elif sort_method == 'max_price':
        phone_objects = Phone.objects.all().order_by('-price')
    else:
        phone_objects = Phone.objects.all()
    template = 'catalog.html'
    context = {'phones': phone_objects}
    return render(request, template, context)


def show_product(request, slug):
    phone_object = Phone.objects.filter(slug=slug)
    template = 'product.html'
    if len(phone_object) > 0:
        context = {'phone': phone_object[0]}
    else:
        context = {}
    return render(request, template, context)
