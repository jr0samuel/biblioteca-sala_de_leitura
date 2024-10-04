from django.contrib import admin
from alunos.models import Aluno, Prof

# Register your models here.

@admin.register(Aluno)
class Aluno(admin.ModelAdmin):
    readonly_fields = ('id', 'nome', 'turma', 'ra', 'senha')

@admin.register(Prof)
class ProfAdmin(admin.ModelAdmin):
    readonly_fields = ('nome', 'senha')
