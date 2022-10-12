from rest_framework import serializers
from .models import Stocking



class stockingserializer(serializers.ModelSerializer):
    class Meta:
        model= Stocking
        fields= ('id','SubCompartment_Name','Date','Surviving','Dead',)
