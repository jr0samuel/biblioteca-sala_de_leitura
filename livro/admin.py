from django.contrib import admin
from .models import Livros

# Register your models here.

# admin.site.register(Livros)
@admin.register(Livros)
class Livros(admin.ModelAdmin):
    list_display = ("autor", "título", "local_Editora_Ano", "quantidade")
