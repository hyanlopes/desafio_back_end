from django.urls import path
from rest_framework.authtoken import views

from . import views as view

urlpatterns = [
    path("store/", view.StoreView.as_view(), name="store"),
    path("store/<str:name>/", view.StoreListView.as_view(), name="unic_store"),
]
