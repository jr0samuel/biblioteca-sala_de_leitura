from django.conf import settings
from django.db import models
from datetime import date
import datetime
from django.db.models.base import Model
from alunos.models import Aluno, Prof

# Create your models here.

class Livros(models.Model):
    img = models.ImageField(upload_to='capa_livro', null=True, blank=True)
    tombo = models.CharField(max_length=20, blank = True, null = True)
    autor = models.CharField(max_length=100, blank = True, null = True)
    título = models.CharField(max_length=100, blank = True, null = True)
    local_Editora_Ano = models.CharField(max_length=100, blank = True, null = True)
    quantidade = models.IntegerField(blank = True, null = True)
    observação = models.CharField(max_length=100, blank = True, null = True)
    data_de_empréstimo = models.CharField(max_length=20, blank = True, null = True)
    data_de_devolução = models.CharField(max_length=20, blank = True, null = True)
    aluno = models.ForeignKey(Aluno, on_delete=models.DO_NOTHING, blank = True, null = True)
    prof = models.ForeignKey(Prof, on_delete=models.DO_NOTHING, blank = True, null = True)

    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.título
