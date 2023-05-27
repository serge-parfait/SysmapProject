from django.db import models
from django.conf import settings
from contracts.models import Contract, Montant

class Event(models.Model):
    libelle = models.fields.CharField(max_length=200)
    dateEvent = models.fields.DateField(null=True, blank=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    authorEv = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        desc = str(self.libelle)+' du '+ str(self.dateEvent)
        return desc

    class Meta:
        ordering = ["dateEvent"]

class Livrable(models.Model):
    class Nature(models.TextChoices):
        FOURNITURES = 'FO'
        TRAVAUX = 'TR'
        SCES_QUANTIFIABLES = 'SQ'
        PRES_INTELLECTUELLE = 'PI'
        CONCEPT_REALISATION = 'CR'
        ACCORD_CADRE = 'AC'
        PLURIANNUEL_TRANCHE = 'PT'
        RESERVE = 'RE'
        SPECIAL = 'SP'
    nature = models.fields.CharField(choices=Nature.choices, max_length=2, default='TR')
    libelle = models.fields.CharField(max_length=200)
    class TypeLivrable(models.TextChoices):
        IMPREVU = 'I'
        ATTENDU = 'A'
    typeLivrable = models.fields.CharField(choices=TypeLivrable.choices ,max_length=1, default='A') 
    isRealized = models.fields.BooleanField(default=False)
    isReceive = models.fields.BooleanField(default=False)
    datValidation = models.fields.DateField(blank=True, null=True)
    event = models.ForeignKey(Event, null=True, on_delete=models.CASCADE)
    authorLi = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.libelle)


class ExecutionContrat(models.Model):
    class EtatExec(models.TextChoices):
        EN_COURS = 1
        NON_DEBUTE = 2
        EN_ARRET = 3
    etatExec = models.fields.IntegerField(choices=EtatExec.choices, default=2)
    txExecPhy = models.fields.IntegerField(null=True)
    nbreAvenant = models.fields.IntegerField(null=True)
    nbreDecompte = models.fields.IntegerField(null=True)
    nbreOs = models.fields.IntegerField(null=True)

class Avenant(models.Model):
    objetAvenant = models.fields.CharField(max_length=250)
    event = models.ForeignKey(Event, blank=True, null=True, on_delete=models.CASCADE)
    montant = models.ForeignKey(Montant, blank=True, on_delete=models.CASCADE)
    dateAvenant = models.fields.DateField(blank=True, null=True)
    authorAv = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        desc = str(self.objetAvenant)+ ' du '+ str(self.dateAvenant)
        return str(desc)

class Ordre_Service(models.Model):
    numerOs = models.fields.CharField(max_length=50, blank=True, null=True)
    motifOs = models.fields.CharField(max_length=250)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    datOs = models.fields.DateField(null=True, blank=True)
    class TypeOs(models.TextChoices):
        DEMARRAGE = 'D'
        SUSPENSION = 'S'
        REPRISE = 'R'
        TECHNIQUE = 'T'
        SUSPENSION_REPRISE = 'SR'
    typeOs = models.fields.CharField(max_length=2, choices=TypeOs.choices, default='D')
    authorOs = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        desc = str(self.get_typeOs_display())+ ' pour '+ str(self.motifOs)
        return str(desc)
 
class Decompte(models.Model):
     numero = models.fields.CharField(max_length=50)
     designation = models.fields.CharField(max_length=200)
     txDecompte = models.fields.IntegerField()
     datDecompte = models.fields.DateField(null=True, blank=True)
     datSignaCsm = models.fields.DateField(null=True, blank=True)
     datSignaIng = models.fields.DateField(null=True, blank=True)
     datSignaMoa = models.fields.DateField(null=True, blank=True)
     montant = models.ForeignKey(Montant, on_delete=models.CASCADE)
     contract = models.ForeignKey(Contract, on_delete=models.CASCADE)  
     authorDe = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)   

class Paiement(models.Model):
    numero = models.fields.CharField(max_length=20)
    class ModEngagement(models.TextChoices):
        BON_ENGAGEMENT = 'BON'
        DECISION_ENGAGEMENT = 'DEC'
    modEngagement = models.fields.CharField(choices=ModEngagement.choices, max_length=3, default="BON")
    datPaiement = models.fields.DateField(null=True, blank=True)
    class ModePaiement(models.TextChoices):
        VIREMENT = 'V'
        EN_ESPECES = 'E'
        INCONNU = 'I'
    modePaiement = models.fields.CharField(choices=ModePaiement.choices, max_length=2, default='I') 
    decompte = models.ForeignKey(Decompte, on_delete=models.CASCADE)
    authorPa = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)    
    
    def __str__(self):
        desc = str(self.get_modePaiement_display())+ ' du bon Numéro '+ str(self.numBonEnga)
        return str(desc)