"""
Definition of models.
"""


from decimal import Rounded
from email.policy import default

from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

from django.forms import PasswordInput
from django.shortcuts import render
from django.urls import reverse

from requests import post
import requests


import UVGV_FMS

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.storage import default_storage
from keras.models import load_model
from keras.preprocessing import image
from keras.utils.image_utils import img_to_array,load_img
import json 
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

img_height, img_width = 224, 224
with open('UVGV_FMS/models/labels.json', 'r') as f:
    labelInfo = f.read()

labelInfo = json.loads(labelInfo)
# print(labelInfo)
np.set_printoptions(suppress=True)
tf.compat.v1.disable_eager_execution()
model_graph = tf.Graph()
with model_graph.as_default():
    tf_session = tf.compat.v1.Session()

    with tf_session.as_default():
        model=load_model('UVGV_FMS/models/keras_model.h5',compile=False)


class Result(models.Model):
    imagepath = models.TextField()
    image = models.ImageField(null=True, blank=True)
    predicted = models.TextField()
    confidence = models.IntegerField(default=0, null=True, blank=True)
    saved = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('saved',)

    def __str__(self):
        return self.imagepath

class pickupload(models.Model):
    image = models.ImageField(upload_to='media/', null=True, blank=True)

    class Meta:
        ordering=['image']

    def __str__(self):
        
        return str(self.image)
        
    def save(self, *args, **kwargs):
        print (self.image.name)
        fileObj= self.image
        filePathName = default_storage.save(fileObj.name, fileObj)
        filePathName = default_storage.path(filePathName)
        data = np.ndarray(shape=(100, 224, 224, 3), dtype=np.float32)
        size = (224, 224)

        img = load_img(filePathName, target_size=(img_height, img_width)).convert('RGB')
        img = ImageOps.fit(img, size, Image.LANCZOS)
        test_image = np.asarray(img)
        nomalisedimg= (test_image.astype(np.float32) / 127.0) - 1

        data[0]= nomalisedimg
        test_image = np.expand_dims(test_image, axis = 0)

        confidence = 0
        with model_graph.as_default():
            with tf_session.as_default():
                pred = model.predict(data)
                # print(pred)
                confidence = round(np.max(pred) * 100, 2)

        predictedLabel = labelInfo[str(np.argmax(pred[0]))]
             # print('Predicted label: ', predictedLabel)  
             # print(f'Confidence : {confidence}%')    



        filename = filePathName.split('/')[-1]
             # print(filename)

        new_item = Result(imagepath = filePathName , image = filename, predicted = predictedLabel, confidence = confidence)
        new_item.save()

        super(pickupload, self).save(*args, **kwargs)

    def lastpick(self,**kwargs):
        chicco=pickupload()
        #print (self.image.name)
        return self.image.name
          
    

    






# Create your models here.


class PlantingSeason(models.Model):
    
    Planting_Season = models.CharField(max_length = 10,primary_key=True)
    def __str__(self):
        return self.Planting_Season
    def __unicode__(self):
       return self.Planting_Season
    
    
class Project(models.Model):
    
    projects=[('LLTC','LLTC'),('IT','IT'),('UVGV','UVGV')]
    Project_Name = models.CharField(max_length = 10, choices=projects,default='I',primary_key=True)

    def __str__(self):
        return self.Project_Name
    def __unicode__(self):
       return self.Project_Name

class WorkingCircle(models.Model):
    
    Usage = models.CharField(max_length = 150,primary_key=True, default='Fuelwood')

    def __str__(self):
        return self.Usage
    def __unicode__(self):
       return self.Usage

class Specie(models.Model):

    Specie = models.CharField(max_length = 150,primary_key=True)
    Vernacular_Name = models.CharField(max_length = 150)
    Standard_Form_Factor = models.FloatField()

    def __str__(self):
        return self.Specie
    def __unicode__(self):
       return self.Specie

class Espacement(models.Model):
    Espacement = models.CharField(max_length = 150,primary_key=True)
    RowSpacing = models.IntegerField()    
    InterRowSpacing = models.IntegerField()
    def __str__(self):
        return self.Espacement
    def __unicode__(self):
       return self.Espacement

class SubCompartmentRegister(models.Model):
    
    SubCompartment_Name = models.CharField(max_length = 10,verbose_name="Block Name ",primary_key=True)
    Compartment_Name = models.CharField(max_length = 10)
    Hectares = models.FloatField()
    Specie = models.ForeignKey(Specie, verbose_name="Specie", on_delete=models.CASCADE,default='Eucalyptus tereticornis',)    
    Planting_Year = models.ForeignKey(PlantingSeason, verbose_name="Planting Season", on_delete=models.CASCADE)
    Project_Name=models.ForeignKey(Project,verbose_name="Project Name", on_delete=models.CASCADE,default='I',)
    WorkingCircles=models.ForeignKey(WorkingCircle,verbose_name="Usage", on_delete=models.CASCADE,default='Fuelwood',)
    Espacement= models.ForeignKey(Espacement, verbose_name="Espacement", on_delete=models.CASCADE,default='3 x 2',)
    
    
    def __str__(self):
        return self.SubCompartment_Name   

    
    def __unicode__(self):
       return self.SubCompartment_Name

    class Meta:
        verbose_name='Compartment Register'
        verbose_name_plural= 'Compartments Register'
        

    

   
    def Stocking_Percentage(self):

        for stockings in (Stocking.objects.filter(SubCompartment_Name=self.SubCompartment_Name,Surviving__isnull=False)):
            if stockings is None:
                return 
            return SubCompartmentRegister.CalculateStocking_Percentage(self)

    def last_Date_Of_Count(self):

        for lastdate in (Stocking.objects.filter(SubCompartment_Name=self.SubCompartment_Name,Surviving__isnull=False)):
            if lastdate is None:
                return 
            return SubCompartmentRegister.calculatelast_Date_Of_Count(self)

    
    def CalculateStocking_Percentage(self,**args,):
        
        if (Stocking.objects.filter(SubCompartment_Name=self.SubCompartment_Name,Surviving__isnull=False).last().Surviving)!=None:
            
            

            survival = (Stocking.objects.filter(SubCompartment_Name=self.SubCompartment_Name,Surviving__isnull=False).last().Surviving)

            treesperhectare = (10000/((Espacement.objects.filter(Espacement=self.Espacement).last().RowSpacing) * 
        (Espacement.objects.filter(Espacement=self.Espacement).last().InterRowSpacing)))
            totaltrees= (self.Hectares* treesperhectare)
            survivalpercentage=round(float(survival/totaltrees),2)
            

            return '{}{}'.format(survivalpercentage*100,'%')

    def calculatelast_Date_Of_Count(self):

        return (Stocking.objects.filter(SubCompartment_Name=self.SubCompartment_Name,Surviving__isnull=False).last().Date)
    


class FlutterUser(models.Model):
    UserName = models.CharField(max_length = 150,primary_key=True)
    Email = models.EmailField(max_length=250)
    Password = models.CharField(max_length = 50)
    

    
    def __str__(self):
        return self.UserName

    


  

class Stocking(models.Model):
    id = models.AutoField(primary_key=True)
    SubCompartment_Name= models.ForeignKey(SubCompartmentRegister, verbose_name="Block Name", on_delete=models.CASCADE,default="15B1S1")
    Date = models.DateField(auto_now_add=True)
    Surviving = models.IntegerField(null=True,)
    Dead = models.IntegerField()
    UserName= models.ForeignKey(FlutterUser, verbose_name='Data Collector', on_delete=models.DO_NOTHING,null=True)

    def __int__(self):
        return self.id
    def __unicode__(self):
       return self.id

    def block(self):
        blockname = (Stocking.objects.filter(Surviving__isnull=False).order_by('Date').first().SubCompartment_Name)
        
        return blockname
    
   
class Volume(models.Model):
    id = models.AutoField(primary_key=True)
    SubCompartment_Name= models.ForeignKey(SubCompartmentRegister, verbose_name="Block Name", on_delete=models.CASCADE,default="15B1S1")
    SampleNo=models.CharField(max_length = 150)
    TreeNo = models.IntegerField()
    DBH = models.IntegerField()
    Height = models.DecimalField(max_digits=9, decimal_places=1,verbose_name="Height")
    UserName= models.ForeignKey(FlutterUser, verbose_name='Data Collector', on_delete=models.DO_NOTHING,null=True)
    
    

    



