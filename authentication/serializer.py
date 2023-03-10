from .models import *
from rest_framework import serializers

class ExpenseUserSerialiser(serializers.ModelSerializer):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    class Meta:
        model=ExpenseUser
        fields='__all__'
    
class PocketMoneySerializer(serializers.ModelSerializer):
    money=models.IntegerField()
    user=models.IntegerField()
    month=models.CharField(max_length=30)
    class Meta:
        model=PocketMoney
        fields='__all__'
        
class BudgetSerializer(serializers.ModelSerializer):
    user=models.IntegerField(null=True)
    expense=models.CharField(max_length=30)
    amount=models.IntegerField()
    month=models.CharField(max_length=30,null=False,default='August')
    
    class Meta:
        model=Budget
        fields='__all__'
