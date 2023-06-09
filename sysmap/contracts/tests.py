from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from contracts.models import Contract

class TestContract(APITestCase):
    # Nous stockons l’url de l'endpoint dans un attribut de classe pour pouvoir l’utiliser plus facilement dans chacun de nos tests
    url = reverse_lazy('contract-list')

    def format_datetime(self, value):
        # Cette méthode est un helper permettant de formater une date en chaine de caractères sous le même format que celui de l’api
        return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    def test_list(self):
        # Créons deux contrats dont un seul est actif
        contrat = Contract.objects.create(object='Construction de immeuble siège MINEPAT', actif=True)
        Contract.objects.create(name='Réfection de la délégation départementale de Nanga Eboko', actif=False)

        # On réalise l’appel en GET en utilisant le client de la classe de test
        response = self.client.get(self.url)
        # Nous vérifions que le status code est bien 200
        # et que les valeurs retournées sont bien celles attendues
        self.assertEqual(response.status_code, 200)
        excepted = [
            {
                'id': contrat.pk,
                'object': contrat.object,
                'dateCreated': self.format_datetime(contrat.dateCreated),
                'datSignaMoa': self.format_datetime(contrat.datSignaMoa),
            }
        ]
        self.assertEqual(excepted, response.json())

    def test_create(self):
        # Nous vérifions qu’aucune catégorie n'existe avant de tenter d’en créer une
        self.assertFalse(Contract.objects.exists())
        response = self.client.post(self.url, data={'object': 'Nouveau contrat'})
        # Vérifions que le status code est bien en erreur et nous empêche de créer un contrat
        self.assertEqual(response.status_code, 405)
        # Enfin, vérifions qu'aucun nouveau contrat n’a été créée malgré le status code 405
        self.assertFalse(Contract.objects.exists())
