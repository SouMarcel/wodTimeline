# Generated by Django 5.0.6 on 2024-05-23 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personagens', '0003_alter_personagem_options_personagem_livro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personagem',
            name='alcunha',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='alcunha'),
        ),
    ]
