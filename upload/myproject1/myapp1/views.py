# views.py
from django.http import HttpResponse
from rest_framework import viewsets
from django.core import serializers
from .serializers import HeroSerializer
from .models import Hero
from .models import Diamond


def list(request):
    queryset = Hero.objects.all()
    queryset = serializers.serialize('json', queryset)
    return HttpResponse(queryset, content_type="application/json")

def list(request):
    queryset = Diamond.objects.all()
    queryset = serializers.serialize('json', queryset)
    return HttpResponse(queryset, content_type="application/json")



