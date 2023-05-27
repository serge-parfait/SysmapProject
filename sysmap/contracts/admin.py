from django.contrib import admin

from .models import Contract, Exercice, Montant, Holder, CommissionMember, Ressource, Guichet

class ContractAdmin(admin.ModelAdmin):
    list_display = ('object', 'numero','delays', 'typePassation','lieuLivraison', 'numLot')

class ExerciceAdmin(admin.ModelAdmin):
    list_display = ('annee', 'codeExo', 'tauxTva', 'tauxIR','autreTax')

class CommissionMemberAdmin(admin.ModelAdmin):
    list_display = ('designation', 'sigle')

class RessourceAdmin(admin.ModelAdmin):
    list_display = ('source', 'code')

class GuichetAdmin(admin.ModelAdmin):
    list_display = ('source', 'guichet', 'imputation')

admin.site.register(Contract, ContractAdmin)
admin.site.register(Exercice, ExerciceAdmin)
admin.site.register(CommissionMember, CommissionMemberAdmin)
admin.site.register(Ressource, RessourceAdmin)
admin.site.register(Guichet, GuichetAdmin)
