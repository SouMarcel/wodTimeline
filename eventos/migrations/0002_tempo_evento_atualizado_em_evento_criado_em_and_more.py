# Generated by Django 5.0.6 on 2024-07-02 00:20

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tempo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('era', models.CharField(max_length=50, verbose_name='Era')),
                ('ano_ini', models.IntegerField(verbose_name='Ano de Início')),
                ('p_ini', models.CharField(blank=True, choices=[('1', 'a.C'), ('2', 'd.C')], max_length=1, null=True, verbose_name='Período de Início')),
                ('ano_fim', models.IntegerField(verbose_name='Ano de Fim')),
                ('p_fim', models.CharField(blank=True, choices=[('1', 'a.C'), ('2', 'd.C')], max_length=1, null=True, verbose_name='Período de Fim')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('criado_em', models.DateField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'tempo',
                'verbose_name_plural': 'tempos',
            },
        ),
        migrations.AddField(
            model_name='evento',
            name='atualizado_em',
            field=models.DateField(auto_now=True, verbose_name='Atualizado em'),
        ),
        migrations.AddField(
            model_name='evento',
            name='criado_em',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Criado em'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='tempo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eventos.tempo', verbose_name='Tempo'),
            preserve_default=False,
        ),
    ]