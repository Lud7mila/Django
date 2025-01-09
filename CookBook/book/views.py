from django.shortcuts import render
from .models import *

def get_cookbook(request):
    context = {"page_name": "Кулинарная книга"}
    return render(request, "Main.html", context)

def get_recipes(request):
    recipes = Recipe.objects.all()
    print(recipes)
    context = {"page_name": "Рецепты",
               'recipes': recipes}
    return render(request, "Content.html", context)

def get_info_about(request):
    context = {"page_name": "Об авторе Кулинарной книги"}
    return render(request, "About.html", context)

