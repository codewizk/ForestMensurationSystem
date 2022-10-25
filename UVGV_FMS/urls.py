from django.urls import path
from .views import ListStocking, detailStocking,ListCompartment,ListFlutterUsers

urlpatterns = [
    path('',ListStocking.as_view),
    path('<int:pk>/',detailStocking.as_view),
    path('/compartments',ListCompartment.as_view),
    path('/flutterusers',ListFlutterUsers.as_view),

    
]
