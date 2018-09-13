from rest_framework import routers
from risk.viewsets import RiskViewSet

router = routers.DefaultRouter()
router.register(r'risk', RiskViewSet)