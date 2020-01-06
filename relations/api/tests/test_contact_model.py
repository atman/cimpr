
from django.contrib.auth import get_user_model

from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

import json

from core.models import Contact


CONTACT_BASE_URL = reverse("relations:contact")
CONTACT_TOKEN_URL = reverse("accounts:obtain-token")
CONTACT_REFRESH_TOKEN_URL = reverse("accounts:refresh-token")


# --------- HELPER FUNCTIONS ------------
def create_user(**params):
    return get_user_model().objects.create_user(**params)

def get_token():
    return

def create_contact(first_name="API Test", email="apitest@test.com", rel_type="M"):

    sample_data = {
        'first_name': first_name,
        'email': email,
        'type': rel_type
    }
    Contact.objects.create()



def get_detail_url(contact_id=1):
    return reverse("relations:contact-detail", args=[contact_id])


class PublicContactAPITest(TestCase):

    def setUp(self):
        self.client = APIClient(self)

    def test_login_required(self):
        """Test if unauthorized requests are not allowed"""
        response_list = self.client.get(CONTACT_BASE_URL)
        response_detail = self.client.get(get_detail_url(2))

        self.assertEqual(response_list.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response_detail.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateContactAPITest(TestCase):

    def setUp(self):
        payload = {
            "username": "admin",
            "password": "admin42"
        }
        self.payload = payload
        create_user(**payload)
        #self.sample_user = get_user_model().objects.get(id=1)
        self.client = APIClient(self)
        #self.client.force_authenticate(self.sample_user)
        self.token_response = self.client.post(CONTACT_TOKEN_URL, payload)

    def test_token_received(self):

        print(str(CONTACT_TOKEN_URL))

        response = self.client.post(CONTACT_TOKEN_URL, self.payload)

        self.assertContains(response, "token")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_token_refreshed(self):

        headers = {"Content-Type": "application/json"}
        #json_payload = json.dumps(self.token_response.data)
        response = self.client.post(CONTACT_REFRESH_TOKEN_URL, self.token_response.data, headers=headers)


        self.assertContains(response, "token")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_contact(self):
        #contact_1 = create_contact(email="sample@test.com")
        #contact_2 = create_contact(email="sample2@test.com")

        #response = self.client.post()
        pass

    def test_contact_api_view_get(self):
        pass




