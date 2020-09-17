from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Client(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE)
	cni  = models.CharField(max_length = 10)
	adress = models.CharField(max_length= 10)
	phone  = models.CharField(max_length=10)
	date  = models.DateField(default=timezone.now)


class Bank_Account:
	number = models.PositiveIntegerField()
	client = models.ManyToManyField(Client)

    def __init__(self): 
        self.balance=0
        return self.balance
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        amount.save() 
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            amount.save() 
        else: 
            print("\n Insufficient balance  ") 
  
       