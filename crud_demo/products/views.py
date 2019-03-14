from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm


def list_products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/products.html', context=context)


def create_product(request):
    product_form = ProductForm(request.POST or None)

    if product_form.is_valid():
        product_form.save()
        return redirect('list_products')

    context = {'product_form': product_form}

    return render(request, 'products/product_form.html', context=context)


def update_product(request, id):
    product = Product.objects.get(id=id)
    product_form = ProductForm(request.POST or None, instance=product)

    if product_form.is_valid():
        product_form.save()
        return redirect('list_products')

    context = {
        'product_form': product_form,
        'product': product
    }

    return render(request, 'products/product_form.html', context=context)


def delete_product(request, id):
    product = Product.objects.get(id=id)

    if request.method == "POST":
        product.delete()
        return redirect('list_products')

    context = {'product': product}

    return render(request, 'products/product_delete_confirm.html', context=context)
