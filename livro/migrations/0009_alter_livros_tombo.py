# Generated by Django 5.1.1 on 2024-09-30 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0008_planilha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='tombo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
