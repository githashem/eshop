from django.shortcuts import render
from django.http import HttpResponseNotFound
from eshop_sliders.models import Slider
from eshop_settings.models import Settings
from eshop_product.models import Product
from eshop_category.models import Category
from utilities.email import EmailService


def footer(request):
    context = {
        'settings': Settings.object()
    }
    return render(request, 'shared/Footer.html', context=context)


def header(request):
    context = {}
    return render(request, 'shared/Header.html', context=context)


def home_page(request):
    sliders = Slider.objects.all()

    # EmailService.send_email('test subject',
    #                         ['PersonalHashem@gmail.com'],
    #                         'email/base.html',
    #                         {'title': 'test', 'description': 'test description'})

    context = {
        "sliders": sliders,
        'categories': Category.objects.all(),
    }

    return render(request, 'home.html', context=context)


def about_page(request):
    context = {
        'settings': Settings.object()
    }
    return render(request, 'about.html', context=context)


def not_found(request, exception=None):
    return render(request, '404.html', {})
