from django.db import models

class Holder(models.Model):
    raisonSociale = models.fields.CharField(max_length=100)
    poBox = models.fields.CharField(max_length=20, null=True)
    phone = models.fields.CharField(max_length=15, null=True)
    numContribuable = models.fields.CharField(max_length=20)
    compteBancaire = models.fields.CharField(max_length=50)
        
    def __str__(self):
        return f'self.raisonSociale'

class Montant(models.Model):
    mtHtax = models.fields.IntegerField(default=0)
    mtTva = models.fields.FloatField(blank=True, null=True)
    mtAir = models.fields.FloatField(blank=True, null=True)
    mtNet = models.fields.FloatField(blank=True, null=True)
    mtTtc = models.fields.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.mtTtc)

class Commission(models.Model):
    president = models.fields.CharField(max_length=50, null=True)
    csm = models.fields.CharField(max_length=50)
    engineer = models.fields.CharField(max_length=50, null=True)
    comptable = models.fields.CharField(max_length=50, null=True)

    def __str__(self):
        return f'self.csm'

class Financement(models.Model):
    class Source(models.TextChoices):
        BUDGET_INVESTISSEMENT_PUBLIC = 'BIP'
        FINANCEMENT_EXTERIEUR = 'FINEX'
    source = models.fields.CharField(choices=Source.choices, max_length=5, default='BIP')
    guichet = models.fields.CharField(max_length=30)
    imputation = models.fields.CharField(max_length=27)

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
    object = models.fields.CharField(max_length=100)
    numero = models.fields.CharField(max_length=50, blank=True)
    delays = models.fields.IntegerField(null=True)
    souscriptionDate = models.fields.DateField(null=True, blank=True)
    lieuLivraison = models.fields.CharField(max_length=100)
    actif = models.fields.BooleanField(default=True)
    consistancy = models.fields.CharField(max_length=200, null=True)
    revisionPrice = models.fields.BooleanField(default=False, blank=True)
    storedTaxation = models.fields.BooleanField(default=True)
    datSignaMoa = models.fields.DateField(null=True, blank=True)
    numLot = models.fields.IntegerField(default=0)
    holder = models.ForeignKey(Holder, null=True, blank=True, on_delete=models.SET_NULL)
    montant = models.ForeignKey(Montant, null=True, blank=True, on_delete=models.SET_NULL)
    commission = models.ForeignKey(Commission, null=True, blank=True, on_delete=models.SET_NULL)
    financement = models.ForeignKey(Financement, null=True, blank=True, on_delete=models.SET_NULL)
    localization = models.ForeignKey(Localization, null=True, blank=True, on_delete=models.SET_NULL)
    caution = models.ForeignKey(Cautionnement, null=True, blank=True, on_delete=models.SET_NULL)
    exercice = models.ForeignKey(Exercice, null=True, blank=True, on_delete=models.SET_NULL)
    class UniteDelai(models.TextChoices):
        JOURS = 'JR'
        MOIS = 'M'
    uniteDelai = models.fields.CharField(choices=UniteDelai.choices, max_length=2, default='JR')
    class TypePassation(models.TextChoices):
        APPEL_OFFRE_NAT_OUVERT = 'AONO'
        APPEL_OFFRE_NAT_RESTREINT = 'AONR'
        PROCEDURE_ACCORD_CADRE = 'AC'
        APPEL_OFFRE_INT_OUVERT = 'AOIO'
        APPEL_OFFRE_INT_RESTREINT = 'AOIR'
        APPEL_OFFRE_NAT_CONCOURS = 'AONC'
        APPEL_OFFRE_INT_CONCOURS = 'AOIC'
        APPEL_OFFRE_2_ETAPES = 'AO2'
        PROCEDURE_GRE_A_GRE = 'GAG'
        PROCEDURE_DEMANDE_COTATION = 'DC'
        PROCEDURE_CONSULT_INDIVIDUELLE = 'CI'
    typePassation = models.fields.CharField(choices=TypePassation.choices, max_length=5, default= 'AONO')

    def __str__(self):
        return f'self.object'

class Livrable(models.Model):
    class Nature(models.TextChoices):
        FOURNITURES = 'FO'
        TRAVAUX = 'TR'
        SCES_QUANTIFIABLE = 'SQ'
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
    contract = models.ForeignKey(Contract, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.libelle)