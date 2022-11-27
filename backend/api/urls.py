from django.urls import path
from .views import *

urlpatterns = [
    path('stats/', test, name='stats'),

    path('frauds/', frauds.as_view(), name='frauds'),
]
