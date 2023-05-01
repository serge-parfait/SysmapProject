from django import forms
from contracts.models import Contract, Montant, Financement, Holder, Commission

class ContractForm(forms.ModelForm):
    object = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-contract', 'placeholder':'Objet du contrat :'}), label='')
    numero = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder':'Numéro du contrat'}), label='')
    delays = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}), label='Delai')
    lieuLivraison = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder':'Lieu de livraison...'}), label='')
    consistancy = forms.CharField(max_length=200, required=False, widget=forms.Textarea(attrs={'class': 'form-control form-control-user', 'placeholder':'Consistence...',}), label='')
    revisionPrice = forms.BooleanField(required=False, widget=forms.CheckboxInput, label='Contrat soumis au régime de révision des prix?')
    storedTaxation = forms.BooleanField(widget=forms.CheckboxInput, label='Contrat Enregistré?')
    numLot = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}), label='Numero de lot')
    souscriptionDate = forms.DateField(required=False, widget=forms.NumberInput(attrs={'class':'form-control', 'type' : 'Date', 'placeholder':'Select a date...'}), label='Date de la Souscription')
    datSignaMoa = forms.DateField(required=False, widget=forms.NumberInput(attrs={'class':'form-control', 'type' : 'Date', 'placeholder':'Select a date...'}), label='Date de signature par le MOA')
    class Meta:
        model = Contract
        fields = ['typePassation', 'object', 'numero','delays', 'uniteDelai', 'lieuLivraison', 'consistancy', 'revisionPrice', 'storedTaxation', 'numLot', 'souscriptionDate', 'datSignaMoa']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['typePassation'].widget.attrs.update({'class': 'form-control'})
        self.fields['uniteDelai'].widget.attrs.update({'class': 'form-control'})
        self.fields['typePassation'].label = ''
        self.fields['uniteDelai'].label = ''
        self.fields['souscriptionDate'].widget.attrs.update({'class': 'form-control'})


class MontantForm(forms.ModelForm):
    class Meta:
        model = Montant
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mtHtax'].widget.attrs.update({'class': 'form-control'})
        self.fields['mtHtax'].label = 'Montant HT'
        self.fields['mtTva'].widget.attrs.update({'class': 'form-control'})
        self.fields['mtTva'].label = 'Montant TVA'
        self.fields['mtAir'].widget.attrs.update({'class': 'form-control'})
        self.fields['mtAir'].label = 'Montant IR'
        self.fields['mtNet'].widget.attrs.update({'class': 'form-control'})
        self.fields['mtNet'].label = 'Montant Net'
        self.fields['mtTtc'].widget.attrs.update({'class': 'form-control'})
        self.fields['mtTtc'].label = 'Montant TTC'
    
class FinanceForm(forms.ModelForm):
    class Meta:
        model = Financement
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['source'].widget.attrs.update({'class': 'form-control'})
        self.fields['source'].label = 'Nature des ressources'
        self.fields['guichet'].widget.attrs.update({'class': 'form-control'})
        self.fields['guichet'].label = 'Guichet de paiement'
        self.fields['imputation'].widget.attrs.update({'class': 'form-control'})
        self.fields['imputation'].label = 'Imputation'

class HolderForm(forms.ModelForm):
    raisonSociale = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Raison Sociale :'}), label='Raison sociale')
    poBox = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Boite postale :'}), label='Boite postale')
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Numéro de téléphone :'}), label='Téléphone')
    numContribuable = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Numéro de contribuable')
    compteBancaire = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Numéro du compte bancaire')
    class Meta:
        model = Holder
        fields = '__all__'

class CommissionForm(forms.ModelForm):
    president = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Président :'}), label='Président')
    csm = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Chef de Service')
    engineer = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Ingénieur')
    comptable = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Comptable-Matières')
    
    class Meta:
        model = Commission
        fields = '__all__'
