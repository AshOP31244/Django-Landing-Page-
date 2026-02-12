from django.urls import path
from . import views
from .views import submit_lead

urlpatterns = [
    path("", views.home, name="home"),
    path("submit-lead/", views.submit_lead, name="submit_lead"),
]
