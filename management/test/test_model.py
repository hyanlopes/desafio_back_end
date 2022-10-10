from management.models import Management
from rest_framework.test import APITestCase
from store.models import Store


class TestModel(APITestCase):
    def setUp(self) -> None:
        store = Store.objects.create(**{"name": "Management Store"})
        management_data = {
            "type": "Financiamento",
            "date": "2019/03/01",
            "value": 14200,
            "cpf": "09620676017",
            "card": "4753****3153",
            "hour": "15:34:53",
            "store_property": "JOÃO MACEDO",
            "store_name": "BAR DO JOÃO",
        }
        self.management = Management.objects.create(**management_data, store_id=store)

    def test_cpf_max_value(self):

        """
        Test to verify the max_length of the management cpf is correct
        """

        max_length = self.management._meta.get_field("cpf").max_length
        self.assertEqual(12, max_length)

    def test_store_id_type(self):

        """
        Test to verify if the id type is equal to uuidField
        """

        type = self.management._meta.get_field("id")._description()

        self.assertEqual(type, "Field of type: UUIDField")
