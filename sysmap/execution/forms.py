from django import forms
from execution.models import Livrable, Event, Ordre_Service, Avenant, Decompte, Paiement

class LivrableForm(forms.ModelForm):
    libelle = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Libelle :')
    isRealized = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}), label='Livrable Réalisé ?:')
    isReceive = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}), label='Livrable Receptionné ?:')
    datValidation = forms.DateField(widget=forms.NumberInput(attrs={'class':'form-control', 'type' : 'Date', 'placeholder':'Select a date...'}), label='Date de validation')
    class Meta:
        model = Livrable
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nature'].widget.attrs.update({'class': 'form-control'})
        self.fields['typeLivrable'].widget.attrs.update({'class': 'form-control'})
        self.fields['nature'].label = 'Nature'
        self.fields['typeLivrable'].label = 'Type de livrable'
        self.fields['event'].widget.attrs.update({'class': 'form-control'})
        self.fields['event'].label = 'Evènement'
    
class OrdreServiceForm(forms.ModelForm):
    class Meta:
        model = Ordre_Service
        fields = '__all__'

class AvenantForm(forms.ModelForm):
    class Meta:
        model = Avenant
        fields = '__all__'

class EventForm(forms.ModelForm):
    libelle = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Libelle :')
    dateEvent = forms.DateField(widget=forms.NumberInput(attrs={'class':'form-control', 'type' : 'Date', 'placeholder':'Select a date...'}), label='Date')
    
    class Meta:
        model = Event
        fields = ['libelle', 'dateEvent']

class DecompteForm(forms.ModelForm):
    class Meta:
        model = Decompte
        exclude = ['contract'] 

class PaiementForm(forms.ModelForm):
    class Meta:
        model = Paiement
        fields = '__all__'