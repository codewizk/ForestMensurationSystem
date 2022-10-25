"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from rest_framework import serializers
from rest_framework import generics
from .models import Stocking, SubCompartmentRegister,FlutterUser
from .serializers import stockingserializer,compartmentregisterserializer,FlutterUserserializer
from rest_framework import viewsets


class ListStocking(viewsets.ModelViewSet):
    queryset= Stocking.objects.all()
    serializer_class= stockingserializer

class ListCompartment(viewsets.ModelViewSet):

    queryset=SubCompartmentRegister.objects.all()
    serializer_class= compartmentregisterserializer

class ListFlutterUsers(viewsets.ModelViewSet):
    queryset=FlutterUser.objects.all()
    serializer_class= FlutterUserserializer


'''' 
class detailStocking(generics.RetrieveUpdateDestroyAPIView):
    queryset= models.Stocking.objects.all()
    serializer= stockingserializer
    
'''

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'UVGV_FMS/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'UVGV_FMS/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'UVGV_FMS/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
