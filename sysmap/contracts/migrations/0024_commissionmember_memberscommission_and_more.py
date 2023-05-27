# Generated by Django 4.1.7 on 2023-05-09 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0023_contract_authorco_contract_chapitre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommissionMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=60, null=True)),
                ('sigle', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MembersCommission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('PR', 'President'), ('CSM', 'Chef Service Marche'), ('ING', 'Ingenieur'), ('CM', 'Comptable'), ('INS', 'Ingenieur Suivi'), ('AUT', 'Autre')], default='ING', max_length=3)),
                ('commissionMember', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contracts.commissionmember')),
            ],
        ),
        migrations.RemoveField(
            model_name='contract',
            name='exercice',
        ),
        migrations.AddField(
            model_name='contract',
            name='exercices',
            field=models.ManyToManyField(to='contracts.exercice'),
        ),
        migrations.RemoveField(
            model_name='contract',
            name='commission',
        ),
        migrations.AlterField(
            model_name='contract',
            name='typePassation',
            field=models.CharField(choices=[('AONO', 'Appel Offre National Ouvert'), ('AONR', 'Appel Offre National Restreint'), ('AC', 'Procedure Accord Cadre'), ('AOIO', 'Appel Offre International Ouvert'), ('AOIR', 'Appel Offre International Restreint'), ('AONC', 'Appel Offre National Concours'), ('AOIC', 'Appel Offre International Concours'), ('AO2', 'Appel Offre 2 Etapes'), ('GAG', 'Procedure Gre A Gre'), ('DC', 'Procedure Demande Cotation'), ('CI', 'Procedure De Consultation Individuelle')], default='AONO', max_length=5),
        ),
        migrations.AlterField(
            model_name='financement',
            name='source',
            field=models.CharField(choices=[('BIP', 'Budget Investissement Public'), ('FINEX', 'Financement Exterieur'), ('PLANU', 'Plan D Urgence')], default='BIP', max_length=5),
        ),
        migrations.DeleteModel(
            name='Commission',
        ),
        migrations.AddField(
            model_name='memberscommission',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contracts.contract'),
        ),
        migrations.AddField(
            model_name='contract',
            name='commission',
            field=models.ManyToManyField(through='contracts.MembersCommission', to='contracts.commissionmember'),
        ),
        migrations.AlterUniqueTogether(
            name='memberscommission',
            unique_together={('contract', 'commissionMember')},
        ),
    ]
