from rest_framework.test import APITestCase
from store.models import Store


class TestsModel(APITestCase):
    def setUp(self) -> None:
        store_data = {"name": "Test store"}
        self.store = Store.objects.create(**store_data)

    def test_store_name_max_length(self):

        """
        Test to verify the max_length of the store name is correct
        """

        max_length = self.store._meta.get_field("name").max_length
        self.assertEqual(max_length, 30)

    def test_store_id_type(self):

        """
        Test to verify if the id type is equal to uuidField
        """

        type = self.store._meta.get_field("id")._description()

        self.assertEqual(type, "Field of type: UUIDField")
