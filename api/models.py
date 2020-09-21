from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import time

def generateAccount():
	return int(time.time())

class Client(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE)
	cni  = models.CharField(max_length = 20)
	adress = models.CharField(max_length= 20)
	phone  = models.CharField(max_length=15)
	date  = models.DateField(default=timezone.now)

	def __str__(self):
		return f"{self.user.first_name} {self.user.last_name}"

class BankAccount(models.Model):
	number = models.PositiveIntegerField(editable=False, default=generateAccount, null=False)
	client = models.ForeignKey(Client, on_delete=models.CASCADE, unique=True)
	balance = models.IntegerField(default=0)

	def __str__(self):
		return f"{self.number}"

class Action(models.Model):
	bank_account = models.ForeignKey(BankAccount, on_delete=models.PROTECT)
	montant = models.IntegerField()
	solde = models.IntegerField(editable=False)
	date = models.DateTimeField(default=timezone.now)
	motif = models.CharField(max_length=20, blank=True)

	def save(self, *args, **kwargs):
		account = self.bank_account
		if account.balance<0 and self.montant<0 : return
		self.populateMotif()
		account.balance += self.montant
		account.save()
		self.solde = account.balance
		super(Action, self).save(*args, **kwargs)

	def populateMotif(self):
		if(self.motif) : return
		if(self.montant < 0):
			self.motif = "retrait"
		else:
			self.motif = "depôt"
