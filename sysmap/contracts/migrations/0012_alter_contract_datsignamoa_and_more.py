# Generated by Django 4.1.7 on 2023-04-07 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0011_alter_contract_caution_alter_contract_commission_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='datSignaMoa',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='souscriptionDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]