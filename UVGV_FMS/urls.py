from django.urls import path
from .views import ListStocking, detailStocking,ListCompartment

urlpatterns = [
    path('',ListStocking.as_view),
    path('<int:pk>/',detailStocking.as_view),
    path('/compartments',ListCompartment.as_view),
    
]
