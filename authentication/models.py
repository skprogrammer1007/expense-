from django.db import models

# Create your models here.
class ExpenseUser(models.Model):
    #user_id = models.IntegerField()
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)

class PocketMoney(models.Model):
    money=models.IntegerField()
    #email = models.EmailField(unique=True)
    month=models.CharField(max_length=30)
    user=models.IntegerField(null=True,unique=True)
    
class Budget(models.Model):
    user=models.IntegerField(null=True)
    expense=models.CharField(max_length=30)
    amount=models.IntegerField()
    month=models.CharField(max_length=30,null=False,default='August')
    
