# Generated by Django 5.0.6 on 2024-05-23 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clas', '0003_rename_criacao_personagens_cla_cria_persona_and_more'),
        ('personagens', '0002_alter_livro_isbn_alter_livro_revisao_and_more'),
        ('users', '0002_alter_edicao_atualizado_em_alter_edicao_criado_em_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personagem',
            options={'verbose_name': 'Personagem', 'verbose_name_plural': 'Personagens'},
        ),
        migrations.AddField(
            model_name='personagem',
            name='livro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.livro', verbose_name='Edição'),
        ),
        migrations.AlterField(
            model_name='personagem',
            name='alcunha',
            field=models.CharField(max_length=100, verbose_name='alcunha'),
        ),
        migrations.AlterField(
            model_name='personagem',
            name='atualizado_em',
            field=models.DateField(auto_now=True, verbose_name='Update'),
        ),
        migrations.AlterField(
            model_name='personagem',
            name='cla',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clas.cla', verbose_name='Cla'),
        ),
        migrations.AlterField(
            model_name='personagem',
            name='criado_em',
            field=models.DateField(auto_now_add=True, verbose_name='Criacao'),
        ),
        migrations.AlterField(
            model_name='personagem',
            name='ficha',
            field=models.URLField(verbose_name='Ficha'),
        ),
        migrations.AlterField(
            model_name='personagem',
            name='mote',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personagem',
            name='nascimento',
            field=models.DateField(verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='personagem',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='nome'),
        ),
        migrations.DeleteModel(
            name='Livro',
        ),
    ]
