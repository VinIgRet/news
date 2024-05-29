from django.urls import path
from humans.views import index

urlpatterns = [
    path('', index),
]