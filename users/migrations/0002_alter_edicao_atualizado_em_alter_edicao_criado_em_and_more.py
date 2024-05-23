# Generated by Django 5.0.6 on 2024-05-23 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edicao',
            name='atualizado_em',
            field=models.DateField(auto_now=True, verbose_name='Update'),
        ),
        migrations.AlterField(
            model_name='edicao',
            name='criado_em',
            field=models.DateField(auto_now_add=True, verbose_name='Criacao'),
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('editora', models.CharField(max_length=100, verbose_name='Editora')),
                ('revisao', models.CharField(blank=True, max_length=50, null=True, verbose_name='Revisão')),
                ('isbn', models.CharField(blank=True, max_length=13, null=True, verbose_name='ISBN')),
                ('criado_em', models.DateField(auto_now_add=True, verbose_name='Criacao')),
                ('atualizado_em', models.DateField(auto_now=True, verbose_name='Update')),
                ('edicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.edicao', verbose_name='Edição')),
            ],
            options={
                'verbose_name': 'livro',
                'verbose_name_plural': 'livros',
            },
        ),
    ]