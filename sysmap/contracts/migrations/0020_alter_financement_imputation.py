# Generated by Django 4.1.7 on 2023-04-11 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0019_alter_holder_comptebancaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financement',
            name='imputation',
            field=models.CharField(max_length=27),
        ),
    ]
