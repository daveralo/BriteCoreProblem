from rest_framework import viewsets
from .models import Risk, Field
from .serializers import RiskSerializer, FieldSerializer
from rest_framework.decorators import detail_route
from rest_framework.response import Response


class RiskViewSet(viewsets.ModelViewSet):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer

    @detail_route()
    def field_list(self, request, pk=None):
        risk = self.get_object()
        fields = Field.objects.filter(risk=risk)
        fields_json = FieldSerializer(fields, many=True)
        return Response(fields_json.data)


class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
