from rest_framework import routers
from risk.viewsets import RiskViewSet, FieldViewSet

router = routers.DefaultRouter()
router.register(r'risk', RiskViewSet)
router.register(r'field', FieldViewSet)
#router.register(r'risk/(?P<risk_id>\d+)/fields', FieldViewSet)
#router.register(r'risk/(?P<risk_id>\d+)/fields', FieldViewSet, base_name = 'land_list')

