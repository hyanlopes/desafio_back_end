from django.urls import path
from rest_framework.authtoken import views

from . import views as view

urlpatterns = [
    path("store/", view.StoreView.as_view()),
    path("store/<str:name>/", view.StoreListView.as_view()),
    path("login/", views.obtain_auth_token, name="login"),
]
