from django.contrib import admin
from .models import *

admin.site.register(New)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', "cost", 'size')
    search_fields = ('title',)
    list_filter = ('size', "cost")
    list_per_page = 20

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', "age")
    search_fields = ('name',)
    list_filter = ('balance', "age")
    list_per_page = 30
    readonly_fields = ("balance", )