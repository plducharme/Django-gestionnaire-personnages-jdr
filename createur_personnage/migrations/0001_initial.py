# Generated by Django 5.1.7 on 2025-03-19 21:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('code', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='ClassePersonnage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ModificateurAttribut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur', models.FloatField()),
                ('attribut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='createur_personnage.attribut')),
                ('classe_personnage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='createur_personnage.classepersonnage')),
            ],
        ),
        migrations.AddField(
            model_name='classepersonnage',
            name='modificateurs',
            field=models.ManyToManyField(to='createur_personnage.modificateurattribut'),
        ),
        migrations.CreateModel(
            name='Personnage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('histoire', models.TextField()),
                ('attributs', models.ManyToManyField(to='createur_personnage.attribut')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='createur_personnage.classepersonnage')),
            ],
        ),
    ]
