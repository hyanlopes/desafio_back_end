from django.urls import reverse
from rest_framework.test import APITestCase
from store.models import Store


class TestsView(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.base_url = reverse("store")
        cls.store_data = {"name": "Test store"}
        cls.store = Store.objects.create(**cls.store_data)

    def test_store_created_with_success(self):
        self.assertIn(self.store_data["name"], self.store.name)
