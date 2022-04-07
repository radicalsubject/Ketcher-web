import json
import pprint
import pandas as pd
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import  csrf_exempt
from tabulate import tabulate
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url

schema_view = get_swagger_view(title='Pastebin API')

def home(request):
    return render(request, 'index.html')

@csrf_exempt
def get_data(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    return JsonResponse([1, 2, 3], safe=False)









