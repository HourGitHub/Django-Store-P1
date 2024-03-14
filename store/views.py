from django.shortcuts import render

from django.shortcuts import get_object_or_404, render

from .models import Category, Product


# Move to context_processors -->
# def categories(request):
#     return {"categories": Category.objects.all()}


# def product_all(request):
#     products = Product.objects.all()
#     return render(request, "store/index.html", {"products": products})


# def product_detail(request, slug):
#     product = get_object_or_404(Product, slug=slug, in_stock=True)
#     return render(request, "store/single.html", {"product": product})


# def category_list(request, category_slug):
#     category = get_object_or_404(Category, slug=category_slug)
#     products = Product.objects.filter(category=category)
#     return render(
#         request,
#         "store/category.html",
#         {"category": category, "products": products},
#     )




def product_all(request):
    products = Product.objects.filter(is_active=True)  # Filter active products
    return render(
        request, "store/index.html", 
        {"products": products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True, in_stock=True)  # Filter active and in-stock products
    return render(
        request, "store/single.html", 
        {"product": product})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category, is_active=True)  # Filter active products in the category
    return render(
        request, "store/category.html", 
        {"category": category, "products": products})
