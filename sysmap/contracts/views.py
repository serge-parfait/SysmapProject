from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import formset_factory
from contracts.models import Contract, Montant, Guichet
from execution.models import Livrable, Decompte, Paiement, Event
from contracts.forms import ContractForm, MontantForm, GuichetForm, HolderForm, MembersCommissionForm

@login_required
def welcome(request):
    contracts = Contract.objects.all()
    somme_montants = 0
    compteur = 0
    somme_livrable = 0
    somme_decompte = 0
    somme_paiement = 0
    for contract in contracts:
        if contract.montant:
            somme_montants = somme_montants + contract.montant.mtTtc
            compteur = compteur+1
        events = Event.objects.filter(contract=contract)
        for event in events:
            livrables = Livrable.objects.filter(event=event)
            if livrables:
                somme_livrable = somme_livrable + livrables.count()
        decomptes = Decompte.objects.filter(contract=contract)
        if decomptes:
            somme_decompte = somme_decompte + decomptes.count()
            for decompte in decomptes:
                paiements = Paiement.objects.filter(decompte=decompte)
                if paiements:
                    somme_paiement = somme_paiement + paiements.count()

    context = {'contracts': contracts, 
               'somme_montants': somme_montants, 
               'compteur': compteur, 
               'somme_livrable': somme_livrable,
               'somme_decompte': somme_decompte,
               'somme_paiement': somme_paiement,
               }
    return render(request, 'contracts/welcome.html', context=context)

@login_required
def contract_list(request):
    contracts = Contract.objects.all()
    somme_montants = 0
    compteur = 0
    holders_abs = 0
    financeurs_abs = 0
    for contract in contracts:
        if contract.montant:
            somme_montants = somme_montants + contract.montant.mtTtc
            compteur = compteur+1
        if not contract.holder:
            holders_abs = holders_abs +1
        if not contract.financement:
            financeurs_abs = financeurs_abs +1
    
    context = {'contracts': contracts, 
               'somme_montants': somme_montants, 
               'compteur': compteur, 
               'holders_abs': holders_abs,
               'financeurs_abs': financeurs_abs,
               }

    return render(
        request,
        'contracts/contract_list.html',
        context=context
    )

@login_required
def contract_detail(request, id):
    contract = Contract.objects.get(id=id)
    return render(
        request,
        'contracts/contract_detail.html',
        {'contract':contract}
    )

@login_required
def montant_detail(request, id):
    contract = Contract.objects.get(id=id)
   #livrable = Livrable.objects.filter(contract=contract)
    return render(
        request,
        'contracts/contract_detail.html',
        {'contract':contract}
    )

@login_required
def contract_create(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.authorCo = request.user
            if request.user.role == "GESTION94":
                contract.chapitre = "94"
            contract.save()
            form.save_m2m()
            return redirect('contract-detail', contract.id)
    else:
        form = ContractForm()
    return render(request,
                  'contracts/contract_create.html',
                 {'form': form})

@login_required
def contract_update(request, id):
    contract = Contract.objects.get(id=id)
    if request.method == 'POST':
        form = ContractForm(request.POST, instance=contract)
        if form.is_valid:
            form.save()
            return redirect('contract-detail', contract.id)
    else:
        form = ContractForm(instance=contract)
    
    return render(request,
                  'contracts/contract_update.html',
                  {'form':form})

@login_required
def contract_disable(request, id):
    contract = Contract.objects.get(id=id)
    if request.method == 'POST':
        contract.actif = False
        contract.save()
        return redirect('contract-list')
    return render(request,
                  'contracts/contract_disable.html',
                  {'contract': contract})

@login_required
def contract_print(request, id):
    contract = Contract.objects.get(id=id)
    contract.actif = False
    contract.save()
    
    return redirect('contract_list')

@login_required
def contract_amount(request, id):
    contract = Contract.objects.get(id=id)
    if request.method == 'POST':
        form = MontantForm(request.POST)
        if form.is_valid():
            contract.montant = form.save()
            contract.save()
            return redirect('contract-detail', contract.id)
    else:
        form = MontantForm()
    
    return render(request,
                  'contracts/contract_add_amount.html',
                 {'form': form, 
                  'contract': contract})

@login_required
def contract_upd_amount(request, id1, id2):
    montant = Montant.objects.get(id=id1)
    contract = Contract.objects.get(id=id2)
    if request.method == 'POST':
        form = MontantForm(request.POST, instance=montant)
        if form.is_valid():
            form.save()
            return redirect('contract-detail', contract.id)
    else:
        form = MontantForm(instance=montant)
    
    return render(request,
                  'contracts/contract_upd_amount.html',
                 {'form': form, 
                  'contract': contract})

@login_required
def contract_finance(request, id):
    contract = Contract.objects.get(id=id)
    if request.method == 'POST':
        form = GuichetForm(request.POST)
        if form.is_valid():
            contract.financement = form.save()
            contract.save()
            return redirect('contract-detail', contract.id)
    else:
        form = GuichetForm()
    
    return render(request,
                  'contracts/contract_add_finance.html',
                  {'form': form,
                  'contract': contract})
        
@login_required
def contract_upd_finance(request, id1, id2):
    guichet = Guichet.objects.get(id=id1)
    contract = Contract.objects.get(id=id2)
    if request.method == 'POST':
        form = GuichetForm(request.POST, instance=guichet)
        if form.is_valid():
            form.save()
            return redirect('contract-detail', contract.id)
    else:
        form = GuichetForm(instance=Guichet)
    
    return render(request,
                  'contracts/contract_upd_finance.html',
                 {'form': form, 
                  'contract': contract})

@login_required
def contract_holder(request, id):
    contract = Contract.objects.get(id=id)
    if request.method == 'POST':
        form = HolderForm(request.POST)
        if form.is_valid():
            contract.holder = form.save()
            contract.save()
            return redirect('contract-detail', contract.id)
    else:
        form = HolderForm()
    
    return render(request,
                  'contracts/contract_add_holder.html',
                  {'form': form,
                  'contract': contract})

@login_required
def contract_commission(request, id):
    contract = Contract.objects.get(id=id)
    commissionFormSet = formset_factory(MembersCommissionForm, extra=4)
    if request.method == 'POST':
       formset = commissionFormSet(request.POST)
       if formset.is_valid:
            for form in formset:
                membersCommission = form.save(commit=False)
                membersCommission.contract = contract
                membersCommission.save()
                contract.commission.add(membersCommission.commissionMember)
                contract.save() 
            return redirect('contract-detail', contract.id)
    else:
       formset = commissionFormSet()

    return render(request,
                  'Contracts/contract_add_commission.html',
                  { 'contract':contract, 'formset':formset})
