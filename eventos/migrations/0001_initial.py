# Generated by Django 5.0.6 on 2024-07-01 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('livros', '0001_initial'),
        ('locais', '0002_alter_local_options'),
        ('personagens', '0003_alter_personagem_ficha_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('resumo', models.CharField(max_length=200, verbose_name='Resumo')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('livro', models.ManyToManyField(to='livros.livro', verbose_name='Livro')),
                ('local', models.ManyToManyField(to='locais.local', verbose_name='Local')),
                ('personagem', models.ManyToManyField(to='personagens.personagem', verbose_name='Personagem')),
            ],
            options={
                'verbose_name': 'evento',
                'verbose_name_plural': 'eventos',
            },
        ),
    ]
