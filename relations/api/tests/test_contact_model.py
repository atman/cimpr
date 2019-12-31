
from django.contrib.auth import get_user_model

from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Contact


CONTACT_BASE_URL = reverse("relations:contact")


# --------- HELPER FUNCTIONS ------------
def create_contact(first_name="API Test", email="apitest@test.com", rel_type="M"):
    sample_user = get_user_model()
    sample_data = {
        'user': 1,
        'first_name': first_name,
        'email': email,
        'type': rel_type
    }


def get_detail_url(contact_id=1):
    return reverse("relations:contact-detail", args=[contact_id])


class PublicContactAPITest(TestCase):

    def setUp(self):
        self.client = APIClient(self)

    def test_login_required(self):
        """Test if unauthorized requests are not allowed"""
        response_list = self.client.get(CONTACT_BASE_URL)
        response_detail = self.client.get(get_detail_url(2))

        print(response_list.data)
        print(response_detail.data)
        self.assertEqual(response_list.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response_detail.status_code, status.HTTP_403_FORBIDDEN)


