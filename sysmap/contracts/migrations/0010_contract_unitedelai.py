# Generated by Django 4.1.7 on 2023-04-07 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0009_contract_exercice_alter_contract_typepassation'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='uniteDelai',
            field=models.CharField(choices=[('JR', 'Jours'), ('M', 'Mois')], default='JR', max_length=2),
        ),
    ]
