from django.conf import settings
from django.db import models

# Create your models here.

class Livros(models.Model):
    img = models.ImageField(upload_to='capa_livro', null=True, blank=True)
    # tombo = models.CharField(max_length=20)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editora_e_ano = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    data_emprestimo = models.DateField(blank = True, null = True)
    data_devolucao = models.DateField(blank = True, null = True)
    # aluno = models.ForeignKey(Aluno, on_delete=models.DO_NOTHING, blank = True, null = True)
    # prof = models.ForeignKey(Prof, on_delete=models.DO_NOTHING, blank = True, null = True)

    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.titulo