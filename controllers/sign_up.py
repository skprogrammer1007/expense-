from django.shortcuts import render
from rest_framework.decorators import api_view
from authentication.models import *
from authentication.serializer import *
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
print('running views')
# Create your views here.expand1/controllers/sign_up.py
@api_view(['POST'])
def sign_up(req):
    print('running')
    jsonData=JSONParser().parse(req)
    serializer=ExpenseUserSerialiser(data=jsonData)
    if serializer.is_valid():
        serializer.save()
        #user=ExpenseUser.objects.get(email=req.GET.get('email'),password=req.GET.get('password'))
        #serializer = ExpenseUserSerialiser(user)
        print(serializer.data)
        return Response({"auth_token":serializer.data['id']})