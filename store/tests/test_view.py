from django.urls import reverse
from rest_framework.test import APITestCase
from store.models import Store


class TestsView(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.base_url = reverse("store")
        cls.store_data = {"name": "Test store"}

    def test_store_created_with_success(self):
        response = self.client.post(self.base_url, data=self.store_data)
        self.assertEqual(201, response.status_code)
