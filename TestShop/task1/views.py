from http.client import HTTPResponse
from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from .forms import UserRegister
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_cookbook(request):
    context = {"page_name": "Кулинарная книга"}
    return render(request, "Main.html", context)

def get_recipes(request):
    recipes = Recipe.objects.all()
    context = {"page_name": "Рецепты",
               'recipes': recipes}
    return render(request, "Content.html", context)

def get_info_about(request):
    context = {"page_name": "Об авторе Кулинарной книги"}
    return render(request, "About.html", context)


def __is_data_form_valid(username, password, repeat_password, age, users):
    info = {}
    for user in users:
        if username == user.name:
            info["error"] = f"Пользователь '{username}' уже существует!"

    if password != repeat_password:
        if not info:
            info["error"] = ''
        info['error'] = '\n'.join([info['error'], 'Пароли не совпадают!'])
    if age < 18:
        if not info:
            info["error"] = ''
        info["error"] = '\n'.join([info['error'], 'Вы должны быть старше 18!'])
    return info


def registration(request):
    info = {}
    form = UserRegister()
    context = {"page_name": "Регистрация"}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = int(form.cleaned_data["age"])

            users = User.objects.all()
            info = __is_data_form_valid(username, password, repeat_password, age, users)

            if not info:
                User.objects.create(name=username, balance=200, age=age)
                context['registered'] = True
                return render(request, "registration.html", context)
        else:
            form = UserRegister()

    context['info'] = info
    context['form'] = form
    return render(request, "registration.html", context)


def news(request):
    new = New.objects.all().order_by('date')
    paginator = Paginator(new, 2)
    page_number = request.GET.get('page')
    try:
        page_news = paginator.page(page_number)
    except PageNotAnInteger:  # указанный параметр page не является целым числом, обращаемся к первой странице
        page_news = paginator.page(1)
    except EmptyPage:
        page_news = paginator.page(paginator.num_pages)

    context = {"page_name": "Новости",
               "page_news": page_news}
    return render(request, "news.html", context)
