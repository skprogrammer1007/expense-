
#import test
from django.http import HttpResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from authentication.models import *
from authentication.serializer import *
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
#from django.core import serializers

#from authentication.models import serializer

@api_view(['GET','POST','PUT'])
def pocket_money(request):
    if(request.method == 'POST'):
        print('running')
        print(request.headers['auth_token'])
        jsonData=JSONParser().parse(request)
        jsonData['user'] = request.headers['auth_token'] 
        print(jsonData)
        serializer=PocketMoneySerializer(data=jsonData)
        if serializer.is_valid():
           serializer.save()
           print(serializer.data)
           return Response({'data : Thanks for showing your pocket money'})
    elif(request.method == 'GET'):
        print(request.headers['auth_token'])
        mine=PocketMoney.objects.get(user=request.headers['auth_token'])
        serializer = PocketMoneySerializer(mine,many=False)
        return Response(serializer.data)
        #serializer=PocketMoneySerializer(data=jsonData)
    else:
        print(request.headers['auth_token'])
        instance = PocketMoney.objects.get(user=request.headers['auth_token'])
        instance.delete()
        print('running')
        print(request.headers['auth_token'])
        jsonData=JSONParser().parse(request)
        jsonData['user'] = request.headers['auth_token'] 
        print(jsonData)
        serializer=PocketMoneySerializer(data=jsonData)
        if serializer.is_valid():
           serializer.save()
           print(serializer.data)
           return Response({'data : Thanks for showing your pocket money'})
        
        
        
        
        
    
           
    
    
    
    