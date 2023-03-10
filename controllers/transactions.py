from django.http import HttpResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from authentication.models import *
from django.core import serializers

@api_view(['GET','POST'])
def transactions(request):
    print(request)
    return Response('Transaction values')