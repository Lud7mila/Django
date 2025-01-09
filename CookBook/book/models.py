from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)  # имя пользователя
    age = models.IntegerField()  # возраст
    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=100)  # название рецепта
    size = models.IntegerField()  # количество просмотров данного рецепта
    description = models.TextField()  # описание необходимых продуктов
    user = models.ManyToManyField(User, related_name='recipes')  # пользователь, приготовивший по данному рецепту
    url = models.URLField()  # url-источник рецепта
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class New(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title