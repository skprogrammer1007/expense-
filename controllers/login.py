from django.shortcuts import render
from rest_framework.decorators import api_view
from  authentication.models import *
from authentication.serializer import *
from rest_framework.response import Response
print('running views')
# Create your views here.

@api_view(['GET'])
def login(req):
    user=ExpenseUser.objects.get(email=req.GET.get('email'),password=req.GET.get('password'))
    serializer = ExpenseUserSerialiser(user)
    print(serializer.data)
    return Response({"auth_token":serializer.data['id']})