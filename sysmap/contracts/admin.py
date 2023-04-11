from django.contrib import admin

from .models import Contract, Exercice, Montant, Holder

class ContractAdmin(admin.ModelAdmin):
    list_display = ('object', 'numero','delays', 'typePassation','lieuLivraison', 'numLot', 'exercice')

class ExerciceAdmin(admin.ModelAdmin):
    list_display = ('annee', 'codeExo', 'tauxTva', 'tauxIR','autreTax')

admin.site.register(Contract, ContractAdmin)
admin.site.register(Exercice, ExerciceAdmin)
