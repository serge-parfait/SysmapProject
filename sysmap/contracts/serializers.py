from rest_framework.serializers import ModelSerializer
from contracts.models import Contract, Holder, MembersCommission, Montant


class HolderSerializer(ModelSerializer):
    class Meta:
        model = Holder 
        fields = ['raisonSociale','representant', 'poBox', 'phone', 'numContribuable', 'compteBancaire']

class MontantSerializer(ModelSerializer):
    class Meta:
        model = Montant 
        fields = ['mtTva','mtAir', 'mtHtax', 'mtNet', 'mtTtc']

class ContractListSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = ['id', 'chapitre', 'object', 'delays', 'datSignaMoa', 'souscriptionDate']

class ContractDetailSerializer(ModelSerializer):
    holder = HolderSerializer()
    montant = MontantSerializer()

    class Meta:
        model = Contract
        fields = ['id', 'chapitre', 'object', 'delays', 'actif', 'datSignaMoa', 'souscriptionDate', 'consistancy', 'holder', 'commission', 'montant', 'financement', 'exercices']