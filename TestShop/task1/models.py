from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=100)  #имя покупателя(username аккаунта)
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # баланс
    age = models.IntegerField()  # возраст

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100)  #название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)  # размер игровых файлов
    description = models.TextField()  # описание
    age_limited = models.BooleanField(default=False)  # ограничение возраста 18+
    buyer = models.ManyToManyField(Buyer, related_name='games')  # покупатель обладающий игрой

    def __str__(self):
        return self.name