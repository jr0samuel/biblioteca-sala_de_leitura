from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    turma = models.CharField(max_length=25)
    ra = models.CharField(max_length=25)
    senha = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"ID: {self.id} | Nome: {self.nome} | Turma: {self.turma} | RA: {self.ra}"

class Prof(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.nome
