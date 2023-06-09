# Generated by Django 4.1.7 on 2023-03-27 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cautionnement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taux', models.IntegerField()),
                ('garant', models.CharField(max_length=15)),
                ('situation', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('president', models.CharField(max_length=15)),
                ('csm', models.CharField(max_length=15)),
                ('ingeneer', models.CharField(max_length=15)),
                ('comptable', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object', models.CharField(max_length=100)),
                ('lieuLivraison', models.CharField(max_length=100)),
                ('Consistancy', models.CharField(max_length=100)),
                ('revisionPrice', models.BooleanField(default=False)),
                ('storedTaxation', models.BooleanField(default=True)),
                ('typePassation', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Financement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=15)),
                ('guichet', models.CharField(max_length=15)),
                ('imputation', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Holder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raisonSociale', models.CharField(max_length=100)),
                ('poBox', models.CharField(max_length=20)),
                ('numContribuable', models.CharField(max_length=20)),
                ('compteBancaire', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Livrable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nature', models.CharField(max_length=15)),
                ('libelle', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=20)),
                ('isRealized', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Localization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localite', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Montant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
