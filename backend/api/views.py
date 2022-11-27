from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *



# Create your views here.
def test(request):
    return HttpResponse("Hello World")

class frauds(APIView):
    def get(self, request):
        frauds = Fraud.objects.all()
        serializer = FraudSerializer(frauds, many=True)
        return Response(serializer.data)