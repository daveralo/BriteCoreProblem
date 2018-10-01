import json
from django.test import RequestFactory, TestCase
from risk.models import Risk, Field
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse


def response_to_json(response):
    str_content = response.content.decode("utf-8")
    return json.loads(str_content)

class ModelTestCase(TestCase):
    """This class defines the test suite for the risk model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.name = "risk_test"
        self.description = "description for the risk"
        self.risk = Risk(name=self.name, description=self.description)

    def test_model_can_create_a_risk(self):
        """Test the risk model can create a risk."""
        old_count = Risk.objects.count()
        self.risk.save()
        new_count = Risk.objects.count()
        self.assertNotEqual(old_count, new_count)



