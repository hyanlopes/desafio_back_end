from django.urls import reverse
from rest_framework.test import APITestCase


class TestsView(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.base_url = reverse("store")
        cls.store_data = {"name": "Test store"}

    def test_store_created_with_success(self):
        response = self.client.post(self.base_url, data=self.store_data)
        self.assertEqual(201, response.status_code)

    def test_list_all_store(self):
        response = self.client.get(self.base_url)
        self.assertListEqual(response.data, [])

    def test_list_especific_store(self):
        self.client.post(self.base_url, self.store_data)
        response = self.client.get(f"/api/store/{self.store_data['name']}/")
        self.assertEqual(200, response.status_code)
