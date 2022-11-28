"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from rest_framework import serializers
from rest_framework import generics
from .models import Stocking, SubCompartmentRegister,FlutterUser,Result,pickupload
from .serializers import stockingserializer,compartmentregisterserializer,FlutterUserserializer,tensorfloeserilalizers,tensorflowapiserializers
from rest_framework import viewsets

from django.core.files.storage import default_storage

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.files.storage import FileSystemStorage

from rest_framework.views import APIView
from rest_framework.response import Response
 

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
with open('./UVGV_FMS/models/labels.json', 'r') as f:
    labelInfo = f.read()

labelInfo = json.loads(labelInfo)
# print(labelInfo)
np.set_printoptions(suppress=True)
tf.compat.v1.disable_eager_execution()
model_graph = tf.Graph()
with model_graph.as_default():
    tf_session = tf.compat.v1.Session()

    with tf_session.as_default():
        model=load_model('./UVGV_FMS/models/keras_model.h5',compile=False)

# Create your views here.
#@receiver(post_save, sender=pickupload)
def index(request,**kwargs):
    return render(request,'index.html')

#@receiver(post_save, sender=pickupload)
def checking(**kwargs):
    print("chicco the great")
    #chicco= pickupload()
    
    
    
        
    

def predictImage(request, **kwargs):
    # print(request)
    # print(request.POST.dict())
    
    '''
    if request.method=="POST":
        fileObj = request.FILES['filePath']
        fs = FileSystemStorage()

        filePathName = default_storage.save(fileObj.name, fileObj)
        filePathName = default_storage.path(filePathName)
        testimage = '.'+filePathName
        print(testimage)
        # print(filePathName)

        # print(type(testimage))

        # if '%20' in testimage:
        #     testimage = fileObj.replace("%20", ' ')
        #     print(testimage)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
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
        print('Predicted label: ', predictedLabel)  
        print(f'Confidence : {confidence}%')    



        filename = filePathName.split('/')[-1]
        print(filename)

        new_item = Result(imagepath = filePathName , image = filename, predicted = predictedLabel, confidence = confidence)
        new_item.save()
            

        context = {'Predicted Label': predictedLabel, 'Confidence %': confidence,'Filename': filename}
        return render(request, 'index.html', {"context":context})
    ''' 
    try:

        if request.method=="POST":
            fileObj = request.FILES['filePath']
           
            

            filePathName = default_storage.save(fileObj.name, fileObj)
            filePathName = default_storage.path(filePathName)
            testimage = '.'+filePathName
             # print(testimage)
        # print(filePathName)

        # print(type(testimage))

        # if '%20' in testimage:
        #     testimage = fileObj.replace("%20", ' ')
        #     print(testimage)
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
            

            context = {'Predicted Label': predictedLabel, 'Confidence %': confidence,'Filename': filename}
            return render(request, 'index.html', {"context":context})

    except:
        context = {'Predicted Label': 'N/A', 'Confidence %': 'N/A','Filename': 'N/A'}

        return render(request, 'index.html',{'context':context})


def viewDataBase(request):
    all_results = Result.objects.all()

    for i in all_results:
        print(i.imagepath)
        break

    # listOfImages = os.listdir('./media/')
    # listOfImagesPath = ['./media/' + i for i in listOfImages]
    context = { 'all_results':all_results}  #  'listOfImagesPath': listOfImagesPath,
    return render(request, 'viewDB.html', {'context':context})

class ListStocking(viewsets.ModelViewSet):
    queryset= Stocking.objects.all()
    serializer_class= stockingserializer

class ListCompartment(viewsets.ModelViewSet):

    queryset=SubCompartmentRegister.objects.all()
    serializer_class= compartmentregisterserializer

class ListFlutterUsers(viewsets.ModelViewSet):
    queryset=FlutterUser.objects.all()
    serializer_class= FlutterUserserializer

class Listvolumeresult(viewsets.ModelViewSet):
    queryset=Result.objects.all()
    serializer_class= tensorfloeserilalizers

class Listtensorflow(viewsets.ModelViewSet):
    queryset=pickupload.objects.all()
    serializer_class= tensorflowapiserializers


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
