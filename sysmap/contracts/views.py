from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import formset_factory
from contracts.models import Contract, Montant, Guichet, Holder
from execution.models import Livrable, Decompte, Paiement, Event
from contracts.forms import ContractForm, MontantForm, GuichetForm, HolderForm, MembersCommissionForm
from contracts.permissions import IsCreatorAuthenticated

from contracts.serializers import ContractDetailSerializer, ContractListSerializer, HolderSerializer

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


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


class MultipleSerializerMixin:
    detail_serializer_class = None
    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()

class ContractViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ContractListSerializer
    detail_serializer_class = ContractDetailSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Contract.objects.all()
    
    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()


class HolderViewset(ModelViewSet):

    serializer_class = HolderSerializer
    permission_classes = [IsCreatorAuthenticated]

    def get_queryset(self):
        return Holder.objects.all()
    
def generate_pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
    textobject = p.beginText()
    textobject.setTextOrigin(inch, inch)
    textobject.setFont("Helvetica", 14)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    contracts = Contract.objects.all()

    lines = []

    for contract in contracts:
        lines.append(contract.object)
        lines.append (str(contract.delays))
        lines.append(contract.numero)
        lines.append(str(contract.datSignaMoa))
        lines.append('###############################')

    for line in lines:
        textobject.textLine(line)
    
    p.drawText(textobject)
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="contracts.pdf")