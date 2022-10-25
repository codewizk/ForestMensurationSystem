from rest_framework import serializers
from .models import Stocking,SubCompartmentRegister,FlutterUser



class stockingserializer(serializers.ModelSerializer):
    class Meta:
        model= Stocking
        fields= ('id','SubCompartment_Name','Date','Surviving','Dead',)

class compartmentregisterserializer(serializers.ModelSerializer):
    class Meta:
        model= SubCompartmentRegister
        fields=('SubCompartment_Name','Hectares','Specie','Planting_Year','Espacement')

class FlutterUserserializer(serializers.ModelSerializer):
    class Meta:
        model= FlutterUser
        fields=('UserName','Email','Password')
