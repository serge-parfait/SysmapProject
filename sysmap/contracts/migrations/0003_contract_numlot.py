# Generated by Django 3.1.3 on 2023-03-28 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0002_auto_20230328_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='numLot',
            field=models.IntegerField(default=0),
        ),
    ]
