from django.contrib import admin
from .models import Livros

# Register your models here.

# admin.site.register(Livros)

@admin.register(Livros)
class Livros(admin.ModelAdmin):
    list_display = ("titulo", "autor", "editora_e_ano", "quantidade")