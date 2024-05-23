# Generated by Django 5.0.6 on 2024-05-23 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clas', '0003_rename_criacao_personagens_cla_cria_persona_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cla',
            name='antecedentes',
            field=models.TextField(blank=True, null=True, verbose_name='Antecedentes'),
        ),
        migrations.AddField(
            model_name='cla',
            name='apelido',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Apelido'),
        ),
        migrations.AddField(
            model_name='cla',
            name='fraquezas',
            field=models.TextField(blank=True, null=True, verbose_name='Fraquezas'),
        ),
        migrations.AddField(
            model_name='cla',
            name='seita',
            field=models.TextField(blank=True, null=True, verbose_name='Seita'),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='efeito',
            field=models.TextField(blank=True, null=True, verbose_name='Efeito'),
        ),
    ]