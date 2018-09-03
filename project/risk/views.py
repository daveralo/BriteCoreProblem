from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from risk.models import Risk
from risk.serializers import RiskSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def risk_list(request):
    """
    List all code risk, or create a new risk.
    """
    if request.method == 'GET':
        risk = Risk.objects.all()
        serializer = RiskSerializer(risk, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RiskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)        

@csrf_exempt
def risk_detail(request, pk):
    """
    Retrieve, update or delete a risk.
    """
    try:
        risk = Risk.objects.get(pk=pk)
    except Risk.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RiskSerializer(risk)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RiskSerializer(risk, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        risk.delete()
        return HttpResponse(status=204)