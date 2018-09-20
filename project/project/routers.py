from rest_framework import routers
from risk.viewsets import RiskViewSet, FieldViewSet

router = routers.DefaultRouter()
router.register(r'risk', RiskViewSet)
router.register(r'field', FieldViewSet)