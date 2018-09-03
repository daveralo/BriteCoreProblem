from django.test import TestCase
from .models import Risk
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class ModelTestCase(TestCase):
    """This class defines the test suite for the risk model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.risk_name = "test"
        self.risk = Risk(name=self.risk_name)

    def test_model_can_create_a_risk(self):
        """Test the risk model can create a risk."""
        old_count = Risk.objects.count()
        self.risk.save()
        new_count = Risk.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.risk_data = {'name': 'test'}
        self.response = self.client.post(
            reverse('create'),
            self.risk_data,
            format="json")

    def test_api_can_create_a_risk(self):
        """Test the api has risk creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)        