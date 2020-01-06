from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from django.contrib.auth import get_user_model
from django.urls import reverse

import json


TOKEN_URL = reverse("accounts:obtain-token")
REFRESH_TOKEN_URL = reverse("accounts:refresh-token")


"""--------------HELPER FUNCTIONS---------"""


def create_user(**payload):
    return get_user_model().objects.create_user(**payload)


class PublicApiTokenTest(TestCase):

    def setUp(self):
        self.client = APIClient(self)

    def test_obtain_token(self):
        payload = {
            "username": "admin",
            "password": "admin42"
        }
        user = create_user(**payload)

        response = self.client.post(TOKEN_URL, payload)
        print(response.data)
        self.assertContains(response, "token")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_refresh_token(self):
        payload = {
            "username": "admin",
            "password": "admin42"
        }
        user = create_user(**payload)
        response = self.client.post(TOKEN_URL, payload)

        headers = {"Content-Type": "application/json"}
        #json_payload = json.dumps(response.data)
        response = self.client.post(REFRESH_TOKEN_URL, response.data, headers=headers)

        self.assertContains(response, "token")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


