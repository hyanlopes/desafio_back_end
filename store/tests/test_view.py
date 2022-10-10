from django.urls import reverse
from rest_framework.test import APITestCase


class TestsView(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.base_url = reverse("store")
        cls.store_data = {"name": "Test store"}

    def test_store_created_with_success(self):

        """
        Test to verify if the store will be created with success using the route
        """

        response = self.client.post(self.base_url, data=self.store_data)
        self.assertEqual(201, response.status_code)

    def test_list_all_store(self):

        """
        Test to verify if all stores regitered will be returned
        """

        response = self.client.get(self.base_url)
        self.assertListEqual(response.data, [])

    def test_list_especific_store(self):

        """
        Test to verify if a unique store by store_name will be returned
        """

        self.client.post(self.base_url, self.store_data)
        response = self.client.get(f"/api/store/{self.store_data['name']}/")
        self.assertEqual(200, response.status_code)
