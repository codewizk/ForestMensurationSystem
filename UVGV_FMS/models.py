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
from django.urls import reverse






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
    

  
  

class Stocking(models.Model):
    id = models.AutoField(primary_key=True)
    SubCompartment_Name= models.ForeignKey(SubCompartmentRegister, verbose_name="Block Name", on_delete=models.CASCADE,default="15B1S1")
    Date = models.DateField(auto_now_add=True)
    Surviving = models.IntegerField(null=True,)
    Dead = models.IntegerField()

    def __int__(self):
        return self.id
    def __unicode__(self):
       return self.id

    def block(self):
        blockname = (Stocking.objects.filter(Surviving__isnull=False).order_by('Date').first().SubCompartment_Name)
        
        return blockname

class FlutterUser(models.Model):
    UserName = models.CharField(max_length = 150,primary_key=True)
    Email = models.EmailField(max_length=250)
    Password = models.CharField(max_length = 50)
    

    
    def __str__(self):
        return self.UserName

    

   

