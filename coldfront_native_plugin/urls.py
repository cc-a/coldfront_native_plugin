from django.urls import path
from . import views

urlpatterns = [
    path("native-plugin/", views.demo_view, name="demo_view")
]
