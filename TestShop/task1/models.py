from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)  # имя пользователя
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # баланс
    age = models.IntegerField()  # возраст

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=100)  # название рецепта
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # примерная цена ингридиетов для рецепта
    size = models.IntegerField()  # количество просмотров данного рецепта
    description = models.TextField()  # описание необходимых продуктов
    age_limited = models.BooleanField(default=False)  # ограничение возраста 18+
    user = models.ManyToManyField(User, related_name='recipes')  # пользователь, приготовивший по данному рецепту

    def __str__(self):
        return self.title


class New(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)