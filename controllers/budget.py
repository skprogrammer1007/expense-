from django.http import HttpResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from authentication.models import *
from authentication.serializer import *
from django.core import serializers
from rest_framework.parsers import JSONParser

@api_view(['GET','POST'])
def budget(request):
    if(request.method == 'POST'):
        print('running')
        print(request.headers['auth_token'])
        jsonData=JSONParser().parse(request)
        jsonData['user'] = request.headers['auth_token'] 
        print(jsonData)
        serializer=BudgetSerializer(data=jsonData)
        if serializer.is_valid():
           serializer.save()
           print(serializer.data)
           return Response({'data : Thanks for showing your Budget'})
    elif(request.method == 'GET'):
        print(request.headers['auth_token'])
        user=request.headers['auth_token']
        month=request.GET.get('month')
        mine=Budget.objects.filter(user=user , month=month)
        serializer = BudgetSerializer(mine,many=True)
        return Response(serializer.data)
        #serializer=PocketMoneySerializer(data=jsonData) 
   
    
    