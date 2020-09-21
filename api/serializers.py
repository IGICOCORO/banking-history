from .models import *
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
	name = serializers.SerializerMethodField()

	def get_name(self,obj):
		return f"{obj.user.first_name} {obj.user.last_name}"

	class Meta:
		model = Client
		fields = "__all__"

class BankAccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = BankAccount
		fields = "__all__"

class ActionSerializer(serializers.ModelSerializer):
	str_montant = serializers.SerializerMethodField()

	def get_str_montant(self,obj):
		return f"+{obj.montant}" if obj.montant>0 else f"{obj.montant}"

	class Meta:
		model = Action
		fields = "__all__"