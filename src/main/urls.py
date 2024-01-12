# Django
from django.urls import path

# Local
from . import (
    views
)

urlpatterns = [
    # main app
    path('', views.main),
    # api
    path('api/', views.api_endpoint),
]
