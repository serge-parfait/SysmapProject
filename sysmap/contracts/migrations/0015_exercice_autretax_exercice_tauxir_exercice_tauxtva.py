# Generated by Django 4.1.7 on 2023-04-10 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0014_rename_actif_contract_actif_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercice',
            name='autreTax',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='exercice',
            name='tauxIR',
            field=models.FloatField(default=2.2, null=True),
        ),
        migrations.AddField(
            model_name='exercice',
            name='tauxTva',
            field=models.FloatField(default=19.25, null=True),
        ),
    ]
