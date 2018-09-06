import json
from django.test import RequestFactory, TestCase
from .models import Risk
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from . import views


def response_to_json(response):
    str_content = response.content.decode("utf-8")
    return json.loads(str_content)

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
        self.factory = RequestFactory()    

    def test_should_return_empty_array(self):
        # when
        request = self.factory.get('/risk/')
        print(request)
        response = views.risk_list(request)
        print(response)
        json_content = response_to_json(response)

        # then
        self.assertEqual(len(json_content), 0)    