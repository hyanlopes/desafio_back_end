import imp

from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from .models import Store
from .serializers import StoreListSerializer, StoreSerializer


class StoreView(generics.ListCreateAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()


class StoreListView(generics.ListAPIView):
    serializer_class = StoreListSerializer

    def get_queryset(self):

        return Store.objects.filter(name=self.kwargs["name"])


# Create your views here.
