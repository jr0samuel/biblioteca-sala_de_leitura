from django.contrib import admin
from .models import Livros

# Register your models here.

@admin.register(Livros)
class Livros(admin.ModelAdmin):
    list_display = ("id", "tombo", "título", "autor", "local_Editora_Ano", "quantidade", "observação")
