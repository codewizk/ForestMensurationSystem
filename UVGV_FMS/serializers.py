from rest_framework import serializers
from .models import Stocking,SubCompartmentRegister,FlutterUser,Result,pickupload



class stockingserializer(serializers.ModelSerializer):
    class Meta:
        model= Stocking
        fields= ('id','SubCompartment_Name','Date','Surviving','Dead','UserName')

class compartmentregisterserializer(serializers.ModelSerializer):
    class Meta:
        model= SubCompartmentRegister
        fields=('SubCompartment_Name','Hectares','Specie','Planting_Year','Espacement')

class FlutterUserserializer(serializers.ModelSerializer):
    class Meta:
        model= FlutterUser
        fields=('UserName','Email','Password')

class tensorfloeserilalizers(serializers.ModelSerializer):
    class Meta:
        model= Result
        fields= ('imagepath','image','predicted','confidence','saved')

class tensorflowapiserializers(serializers.ModelSerializer):
    class Meta:
        model=pickupload
        fields= "__all__"
