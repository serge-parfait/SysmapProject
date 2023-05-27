from django.conf import settings
from django.db import models

class Holder(models.Model):
    raisonSociale = models.fields.CharField(max_length=100)
    representant = models.fields.CharField(max_length=100, default="inconnu")
    poBox = models.fields.CharField(max_length=20, null=True)
    phone = models.fields.CharField(max_length=15, null=True)
    numContribuable = models.fields.CharField(max_length=20)
    compteBancaire = models.fields.CharField(max_length=50)
        
    def __str__(self):
        desc = str(self.raisonSociale)
        return desc

class Montant(models.Model):
    mtHtax = models.fields.IntegerField(default=0)
    mtTva = models.fields.FloatField(blank=True, null=True)
    mtAir = models.fields.FloatField(blank=True, null=True)
    mtNet = models.fields.FloatField(blank=True, null=True)
    mtTtc = models.fields.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.mtTtc)

class CommissionMember(models.Model):
    designation = models.fields.CharField(max_length=60, null=True)
    sigle = models.fields.CharField(max_length=10)

    def __str__(self):
        desc = str(self.designation)+': '+ str(self.sigle)
        return str(desc)

class Ressource(models.Model):
    source = models.fields.CharField(max_length=50, default="BUDGET D'INVESTISSEMENT PUBLIC")
    code = models.fields.CharField(max_length=5, default="BIP")
    
    def __str__(self):
        return str(self.imputation)

class Guichet(models.Model):
    source = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    guichet = models.fields.CharField(max_length=30, default="Paierie Générale du Trésor")
    imputation = models.fields.CharField(max_length=27, null=True)

    def __str__(self):
        return str(self.imputation)

class Localization(models.Model):
    localite = models.fields.CharField(max_length=15, blank=True)

    def __str__(self):
        return f'self.localite'

class Cautionnement(models.Model):
    taux = models.fields.IntegerField()
    garant = models.fields.CharField(max_length=15)
    situation = models.fields.BooleanField(default=False)

    def __str__(self):
        return f'self.garant'

class Exercice(models.Model):
    annee = models.fields.IntegerField()
    codeExo = models.fields.IntegerField(null=True, blank=True)
    tauxTva = models.fields.FloatField(null=True, default=19.25)
    tauxIR = models.fields.FloatField(null=True, default=2.2)
    autreTax = models.fields.FloatField(null=True, blank=True)
    def __str__(self):
        return str(self.annee)
   
class Contract(models.Model):
    class Chapitre(models.TextChoices):
        INTERVENTION_EN_INVESTISSEMENT = "94"
        ECONOMIE_PLANIFICATION_ET_AMENAGEMENT_DU_TERRITOIRE = "22"
    chapitre = models.fields.CharField(choices=Chapitre.choices, max_length=2, default="22")
    object = models.fields.CharField(max_length=200)
    numero = models.fields.CharField(max_length=50, blank=True)
    delays = models.fields.IntegerField(null=True)
    souscriptionDate = models.fields.DateField(null=True, blank=True)
    lieuLivraison = models.fields.CharField(max_length=100)
    actif = models.fields.BooleanField(default=True)
    consistancy = models.fields.CharField(max_length=300, null=True)
    revisionPrice = models.fields.BooleanField(default=False, blank=True)
    storedTaxation = models.fields.BooleanField(default=True)
    urgencyProcess = models.fields.BooleanField(default=False)
    datSignaMoa = models.fields.DateField(null=True, blank=True)
    numLot = models.fields.IntegerField(null=True, default=0)
    authorCo = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    dateCreated = models.DateField(auto_now=True, null=True)
    holder = models.ForeignKey(Holder, null=True, blank=True, on_delete=models.SET_NULL)
    montant = models.ForeignKey(Montant, null=True, blank=True, on_delete=models.SET_NULL)
    commission = models.ManyToManyField(CommissionMember, through='MembersCommission')
    financement = models.ForeignKey(Guichet, null=True, blank=True, on_delete=models.SET_NULL)
    localization = models.ForeignKey(Localization, null=True, blank=True, on_delete=models.SET_NULL)
    caution = models.ForeignKey(Cautionnement, null=True, blank=True, on_delete=models.SET_NULL)
    exercices = models.ManyToManyField(Exercice)
    class UniteDelai(models.TextChoices):
        JOURS = 'JR'
        MOIS = 'M'
    uniteDelai = models.fields.CharField(choices=UniteDelai.choices, max_length=2, default='M')
    class TypePassation(models.TextChoices):
        APPEL_OFFRE_NATIONAL_OUVERT = 'AONO'
        APPEL_OFFRE_NATIONAL_RESTREINT = 'AONR'
        PROCEDURE_ACCORD_CADRE = 'AC'
        APPEL_OFFRE_INTERNATIONAL_OUVERT = 'AOIO'
        APPEL_OFFRE_INTERNATIONAL_RESTREINT = 'AOIR'
        APPEL_OFFRE_NATIONAL_CONCOURS = 'AONC'
        APPEL_OFFRE_INTERNATIONAL_CONCOURS = 'AOIC'
        APPEL_OFFRE_2_ETAPES = 'AO2'
        PROCEDURE_GRE_A_GRE = 'GAG'
        PROCEDURE_DEMANDE_COTATION = 'DC'
        PROCEDURE_DE_CONSULTATION_INDIVIDUELLE = 'CI'
    typePassation = models.fields.CharField(choices=TypePassation.choices, max_length=5, default= 'AONO')
    numeroPassation = models.fields.CharField(max_length=100, default="inconnu")

    def __str__(self):
        desc = str(self.object)
        return desc


class MembersCommission(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    commissionMember = models.ForeignKey(CommissionMember, on_delete=models.CASCADE)
    class Role(models.TextChoices):
        PRESIDENT = "PR"
        CHEF_SERVICE_MARCHE = "CSM"
        INGENIEUR = "ING"
        COMPTABLE = "CM"
        INGENIEUR_SUIVI = "INS"
        AUTRE = "AUT"
    role = models.fields.CharField(choices=Role.choices, max_length=3, default="ING")

    class Meta:
        unique_together = ('contract', 'commissionMember')
    
    def __str__(self):
        desc = str(self.role)
        return desc