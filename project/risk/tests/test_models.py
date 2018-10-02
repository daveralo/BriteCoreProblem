from django.test import RequestFactory, TestCase
from risk.models import Risk, Field


class ModelTestCase(TestCase):

    def setUp(self):
        """Define test variables."""
        self.name = "risk_test"
        self.description = "description for the risk"
        self.risk = Risk(name=self.name, description=self.description)

    def test_model_can_create_a_risk(self):
        """Test the risk model can create a risk."""
        old_count = Risk.objects.count()
        self.risk.save()
        new_count = Risk.objects.count()
        self.assertNotEqual(old_count, new_count)
