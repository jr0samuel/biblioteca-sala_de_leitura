from django.db.models import fields
from django import forms
from .models import Livros, Planilha

class CadastroLivro(forms.ModelForm):
    class Meta:
        model = Livros
        fields = ('img', 'tombo', 'autor', 'título', 'local_Editora_Ano', 'quantidade', 'observação', 'prof')

class PlanilhaForm(forms.ModelForm):
    class Meta:
        model = Planilha
        fields = ('arquivo', 'planilha')
