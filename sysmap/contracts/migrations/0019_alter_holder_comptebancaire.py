# Generated by Django 4.1.7 on 2023-04-11 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0018_montant_mtair_montant_mthtax_montant_mtnet_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holder',
            name='compteBancaire',
            field=models.CharField(max_length=50),
        ),
    ]