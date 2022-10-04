from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from .models import Store
from .serializers import StoreSerializer


class StoreView(generics.ListCreateAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()


# Create your views here.
