# Generated by Django 2.0.4 on 2018-04-11 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epsiProject', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipe',
            old_name='etudiants',
            new_name='Etudiants',
        ),
        migrations.RenameField(
            model_name='messageequipe',
            old_name='projet',
            new_name='Projet',
        ),
        migrations.RenameField(
            model_name='messageintervenant',
            old_name='projet',
            new_name='Projet',
        ),
    ]
