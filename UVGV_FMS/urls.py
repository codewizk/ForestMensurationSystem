from django.urls import path
from .views import ListStocking, detailStocking

urlpatterns = [
    path('',ListStocking.as_view),
    path('<int:pk>/',detailStocking.as_view),
    
]
