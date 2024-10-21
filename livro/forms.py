from django.db.models import fields
from django import forms
from .models import Livros

class CadastroLivro(forms.ModelForm):
    class Meta:
        model = Livros
        fields = ('digital', 'tombo', 'autor', 'título', 'local_Editora_Ano', 'quantidade', 'observação', 'prof')
