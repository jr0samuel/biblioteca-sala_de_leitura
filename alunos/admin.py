from django.contrib import admin
from alunos.models import Aluno, Prof

# Register your models here.

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    readonly_fields = ('nome', 'turma', 'ra', 'senha')

@admin.register(Prof)
class ProfAdmin(admin.ModelAdmin):
    readonly_fields = ('nome', 'senha')
