from risk.models import Risk, Field
from rest_framework.test import APITestCase


class ViewTestCase(APITestCase):
    def setUp(self):
        """Define test variables."""
        self.name = "risk_test"
        self.description = "description for the risk"
        self.risk = Risk(name=self.name, description=self.description)
        self.risk.save()

    def test_view_url_exists(self):
        """Test view for url."""
        response = self.client.get('/api/risk/')
        self.assertEqual(response.status_code, 200)

    def test_getting_risk(self):
        """Test view get a risk."""
        response = self.client.get('/api/risk/', format="json")
        self.assertEqual(len(response.data), 1)
