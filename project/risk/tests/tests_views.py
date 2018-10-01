#import json
#from django.test import RequestFactory, TestCase
from risk.models import Risk, Field
from rest_framework.test import APITestCase
#from rest_framework import status
#from django.urls import reverse
from django.shortcuts import reverse
#from risk import viewsets



class ViewTestCase(APITestCase):
    def setUp(self):
        #self.factory = RequestFactory()    
        self.name = "risk_test"
        self.description = "description for the risk"
        self.risk = Risk(name=self.name, description=self.description)

    #def test_should_return_empty_array(self):
        # when
        #request = self.factory.get('/api/risk/')
        #print(request)
        #response = viewsets.risk_list(request)
        #print(response)
        #json_content = response_to_json(response)

        # then
        #self.assertEqual(len(json_content), 0)    

    def test_view_url_exists(self):
        response = self.client.get('/api/risk/')
        self.assertEqual(response.status_code, 200)   

    def test_risk_creation(self):
        response = self.client.post(reverse('risk'), {
            'name': 'automobile',
            'description': 'Risk for automobile insurance'
        })

        # assert new movie was added
        self.assertEqual(Risk.objects.count(), 2)

        # assert a created status code was returned
        self.assertEqual(201, response.status_code)        



