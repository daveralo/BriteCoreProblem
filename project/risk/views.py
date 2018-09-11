from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from risk.models import Risk
from risk.serializers import RiskSerializer
#from django.template.loader import render_to_string
#from rest_framework.renderers import TemplateHTMLRenderer
from django.template import loader

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer()
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def risk_list(request):
    """
    List all code risk, or create a new risk.
    """
    if request.method == 'GET':
        risks = Risk.objects.all()
        serializer = RiskSerializer(risks, many=True)
        #context['serializer.data'] = render_to_string("risk/iandex.html")
        #print("daniel")
        #return HttpResponse(json.dumps(context), content_type="application/json")
        #return JSONResponse(serializer.data)  #--ojo original
        template = loader.get_template('index.html')
        context = {'risks': risks,}
        return HttpResponse(template.render(context, request))

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
