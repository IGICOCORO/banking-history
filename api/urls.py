from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register("client", ClientViewset)
router.register("account", BankAccountViewset)
router.register("action", ActionViewset)

urlpatterns = [
	path("", include(router.urls)),
]
