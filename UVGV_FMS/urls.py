from django.urls import path
from .views import ListStocking, detailStocking,ListCompartment,ListFlutterUsers,Listvolumeresult,Listtensorflow
from . import views

urlpatterns = [
    path('',ListStocking.as_view),
    path('<int:pk>/',detailStocking.as_view),
    path('/compartments',ListCompartment.as_view),
    path('/flutterusers',ListFlutterUsers.as_view),
    path('/results',Listvolumeresult.as_view),
    path('/tensorapi',Listtensorflow.as_view),
   

]
