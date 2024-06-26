# Generated by Django 5.0.6 on 2024-05-27 22:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('nivel', models.SmallIntegerField(verbose_name='Nível')),
                ('disciplina', models.CharField(max_length=50, verbose_name='Disciplina')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('sistema', models.TextField(verbose_name='Sistema')),
                ('efeito', models.TextField(blank=True, null=True, verbose_name='Efeito')),
                ('criado_em', models.DateField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateField(auto_now=True, verbose_name='Atualizado em')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livros.livro', verbose_name='Livro')),
            ],
            options={
                'verbose_name': 'disciplina',
                'verbose_name_plural': 'disciplinas',
            },
        ),
    ]
