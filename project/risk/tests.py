import json
from django.test import RequestFactory, TestCase
from .models import Risk, Field
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from . import viewsets


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

class ViewTestCase(TestCase):
    """Test suite for the api views."""
    def setUp(self):
        self.factory = RequestFactory()    

    #def test_should_return_empty_array(self):
        # when
        #request = self.factory.get('/api/risk/')
        #print(request)
        #response = viewsets.risk_list(request)
        #print(response)
        #json_content = response_to_json(response)

        # then
        #self.assertEqual(len(json_content), 0)    

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/api/risk/')
        self.assertEqual(response.status_code, 200)    
