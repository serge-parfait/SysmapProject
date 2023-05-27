from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django import forms
from contracts.models import Contract
from execution.models import Event, Decompte, Livrable, Ordre_Service, Avenant, Paiement
from execution.forms import LivrableForm, EventForm, OrdreServiceForm, AvenantForm, DecompteForm, PaiementForm

@login_required
def follow_tech_contract(request, id):
    contract = Contract.objects.get(id=id)
    events = Event.objects.filter(contract=contract).order_by("dateEvent")
    dico_livrables = {}
    dico_ordres = {}
    dico_avenants = {}
    for event in events:
        livrables = Livrable.objects.filter(event=event)
        ordres_service = Ordre_Service.objects.filter(event=event)
        avenants = Avenant.objects.filter(event=event)
        if len(livrables) > 0:
            dico_livrables[event] = livrables
        if len(ordres_service) > 0:
            dico_ordres[event] = ordres_service
        if len(avenants) > 0:
            dico_avenants[event] = avenants
    
    context = {'events': events, 
               'contract': contract, 
               'dico_livrables': dico_livrables, 
               'dico_ordres': dico_ordres,
               'dico_avenants': dico_avenants,
               }

    return render(request,
                  'execution/follow_tech_contract.html',
                  context= context)

@login_required
def follow_fi_contract(request, id):
    contract = Contract.objects.get(id=id)
    decomptes = Decompte.objects.filter(contract=contract).order_by("datDecompte")
    dico_paiements = {}
    for decompte in decomptes:
        paiements = Paiement.objects.filter(decompte=decompte)
        if len(paiements) > 0:
            dico_paiements[decompte] = paiements
    
    context = {
               'contract': contract,
               'decomptes': decomptes, 
               'dico_paiements': dico_paiements, 
               }

    return render(request,
                  'execution/follow_fi_contract.html',
                  context= context)

@login_required
def create_event(request, id):
    contract = Contract.objects.get(id=id)
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid:
            event = form.save(commit=False)
            event.contract = contract
            event.authorEv = request.user
            event.save()
            return redirect('follow-tech-contract', contract.id)
    else:
        form = EventForm()

    return render(request,
                  'execution/contract_add_event.html',
                  {'form': form, 'contract':contract})

@login_required
def create_livrable(request, id):
    contract = Contract.objects.get(id=id)
    if request.method == 'POST':
        form = LivrableForm(request.POST)
        if form.is_valid:
            livrable = form.save(commit=False)
            livrable.authorLi = request.user
            livrable.save()
            return redirect('follow-tech-contract', contract.id)
    else:
        form = LivrableForm()
        form.fields['event'] = forms.ModelChoiceField(Event.objects.filter(contract=contract))
        form.fields['event'].label = "Evènement"
        form.fields['event'].widget.attrs.update({'class': 'form-control'})
    return render(request,
                  'execution/event_add_livrable.html',
                  {'form': form, 'contract':contract})

@login_required
def create_ordre_service(request, id):
    contract = Contract.objects.get(id=id)
    if request.method == 'POST':
        form = OrdreServiceForm(request.POST)
        if form.is_valid:
            ordre_service = form.save(commit=False)
            ordre_service.authorOs = request.user
            ordre_service.save()
            return redirect('follow-tech-contract', contract.id)
    else:
        form = OrdreServiceForm()
        form.fields['event'] = forms.ModelChoiceField(Event.objects.filter(contract=contract))
        form.fields['event'].label = 'Evènement'
        form.fields['event'].widget.attrs.update({'class': 'form-control'})

    return render(request,
                  'execution/event_add_ordre_service.html',
                  {'form': form, 'contract':contract})

@login_required
def create_avenant(request, id):
    contract = Contract.objects.get(id=id)
    if request.method == 'POST':
        form = AvenantForm(request.POST)
        if form.is_valid:
            avenant = form.save(commit=False)
            avenant.authorAv = request.user
            avenant.save()
            return redirect('follow-tech-contract', contract.id)
    else:
        form = AvenantForm()
        form.fields['event'] = forms.ModelChoiceField(Event.objects.filter(contract=contract))
        form.fields['event'].label = 'Evènement'
        form.fields['event'].widget.attrs.update({'class': 'form-control'})

    return render(request,
                  'execution/event_add_avenant.html',
                  {'form': form, 'contract':contract})

@login_required
def event_detail(request, id):
    event = Event.objects.get(id=id)
    context = {'event': event,
                }
    return render(request, 'execution/event_detail.html', context=context)

@login_required
def create_decompte(request, id):
    contract = Contract.objects.get(id=id)
    if request.method == 'POST':
        form = DecompteForm(request.POST)
        if form.is_valid:
            decompte = form.save(commit=False)
            decompte.contract = contract
            decompte.authorDe = request.user
            decompte.save()
            return redirect('follow-fi-contract', contract.id)
    else:
        form = DecompteForm()

    return render(request,
                  'execution/contract_add_decompte.html',
                  {'form': form, 'contract':contract})

@login_required
def create_paiement(request, id):
    decompte = Decompte.objects.get(id=id)
    contract = decompte.contract
    if request.method == 'POST':
        form = PaiementForm(request.POST)
        if form.is_valid:
            paiement = form.save(commit=False)
            paiement.decompte = decompte
            paiement.authorPa = request.user
            paiement.save()
            return redirect('follow-fi-contract', contract.id)
    else:
        form = PaiementForm()

    return render(request,
                  'execution/contract_add_paiement.html',
                  {'form': form, 'contract':contract})

@login_required
def decompte_detail(request, id):
    decompte = Decompte.objects.get(id=id)
    context = {'decompte': decompte,
                }
    return render(request, 'execution/decompte_detail.html', context=context)