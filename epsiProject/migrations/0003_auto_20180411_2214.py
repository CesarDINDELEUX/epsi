# Generated by Django 2.0.4 on 2018-04-11 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epsiProject', '0002_auto_20180411_2213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipe',
            old_name='Etudiants',
            new_name='etudiants',
        ),
        migrations.RenameField(
            model_name='messageequipe',
            old_name='Projet',
            new_name='projet',
        ),
        migrations.RenameField(
            model_name='messageintervenant',
            old_name='Projet',
            new_name='projet',
        ),
    ]
