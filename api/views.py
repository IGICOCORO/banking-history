from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import *
from .serializers import *

class ClientViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, JWTAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Client.objects.all()
	serializer_class = ClientSerializer

class BankAccountViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, JWTAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = BankAccount.objects.all()
	serializer_class = BankAccountSerializer

	@action(["GET"], False, r"myaccount", "myaccount")
	def myAccountInfo(self, request):
		queryset = BankAccount.objects.get(client=request.user.client)
		serializer = BankAccountSerializer(queryset, many=False)
		return Response(serializer.data)

class ActionViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, JWTAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Action.objects.all()
	serializer_class = ActionSerializer

	@action(["GET"], False, r"myactions", "myactions")
	def myActions(self, request):
		queryset = Action.objects.filter(bank_account=request.user.client.bankaccount)
		serializer = ActionSerializer(queryset, many=True)
		return Response(serializer.data)