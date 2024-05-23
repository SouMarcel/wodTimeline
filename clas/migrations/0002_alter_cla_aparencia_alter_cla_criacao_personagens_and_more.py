# Generated by Django 5.0.6 on 2024-05-23 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cla',
            name='aparencia',
            field=models.TextField(blank=True, null=True, verbose_name='Aparência'),
        ),
        migrations.AlterField(
            model_name='cla',
            name='criacao_personagens',
            field=models.TextField(blank=True, null=True, verbose_name='Criação de Personagens'),
        ),
        migrations.AlterField(
            model_name='cla',
            name='estereotipos',
            field=models.TextField(blank=True, null=True, verbose_name='Estereótipos'),
        ),
        migrations.AlterField(
            model_name='cla',
            name='historia',
            field=models.TextField(blank=True, null=True, verbose_name='História'),
        ),
        migrations.AlterField(
            model_name='cla',
            name='mote',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Mote'),
        ),
        migrations.AlterField(
            model_name='cla',
            name='organizacao',
            field=models.TextField(blank=True, null=True, verbose_name='Organização'),
        ),
        migrations.AlterField(
            model_name='cla',
            name='refugio',
            field=models.TextField(blank=True, null=True, verbose_name='Refúgio'),
        ),
    ]