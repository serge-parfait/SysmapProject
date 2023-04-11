from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from contracts.models import Contract, Montant, Financement
from contracts.forms import ContractForm, MontantForm, FinanceForm, HolderForm, CommissionForm

def welcome(request):
    return render(request, 'contracts/welcome.html')

def contract_list(request):
    contracts = Contract.objects.all()
    return render(
        request,
        'contracts/contract_list.html',
        {'contracts':contracts}
    )

def contract_detail(request, id):
    contract = Contract.objects.get(id=id)
    return render(
        request,
        'contracts/contract_detail.html',
        {'contract':contract}
    )

def montant_detail(request, id):
    contract = Contract.objects.get(id=id)
    return render(
        request,
        'contracts/contract_detail.html',
        {'contract':contract}
    )

def contract_create(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            print(f'le formulaire est valide')
            contract = form.save()
            return redirect('contract-detail', contract.id)
    else:
        form = ContractForm()
    return render(request,
                  'contracts/contract_create.html',
                 {'form': form})

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

def contract_disable(request, id):
    contract = Contract.objects.get(id=id)
    if request.method == 'POST':
        contract.actif = False
        contract.save()
        return redirect('contract-list')
    return render(request,
                  'contracts/contract_disable.html',
                  {'contract': contract})

def contract_print(request, id):
    contract = Contract.objects.get(id=id)
    contract.actif = False
    contract.save()
    
    return redirect('contract_list')

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

def contract_finance(request, id):
    contract = Contract.objects.get(id=id)
    if request.method == 'POST':
        form = FinanceForm(request.POST)
        if form.is_valid():
            contract.financement = form.save()
            contract.save()
            return redirect('contract-detail', contract.id)
    else:
        form = FinanceForm()
    
    return render(request,
                  'contracts/contract_add_finance.html',
                  {'form': form,
                  'contract': contract})
        

def contract_upd_finance(request, id1, id2):
    financement = Financement.objects.get(id=id1)
    contract = Contract.objects.get(id=id2)
    if request.method == 'POST':
        form = FinanceForm(request.POST, instance=financement)
        if form.is_valid():
            form.save()
            return redirect('contract-detail', contract.id)
    else:
        form = FinanceForm(instance=financement)
    
    return render(request,
                  'contracts/contract_upd_finance.html',
                 {'form': form, 
                  'contract': contract})

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

def contract_commission(request, id):
    contract = Contract.objects.get(id=id)
    if request.method == 'POST':
        form = CommissionForm(request.POST)
        if form.is_valid:
            contract.commission = form.save()
            contract.save()
            return redirect('contract-detail', contract.id)
    else:
        form = CommissionForm()

    return render(request,
                  'Contracts/contract_add_commission.html',
                  {'form': form, 'contract':contract})