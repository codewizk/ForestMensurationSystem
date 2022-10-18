"""
Definition of urls for ForestMensurationSystem.
"""

from datetime import datetime
from django.urls import include,path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from UVGV_FMS import forms, views
import UVGV_FMS 
from rest_framework import routers

admin.site.site_header = 'Forest Mensuration System'
admin.site.index_title = 'Forest Mensuration System Administration'
admin.site.site_title = "FMS"

router = routers.DefaultRouter(trailing_slash=False)
router.register('ListStockingdetails', views.ListStocking)
router.register('ListCompartmentdetails',views.ListCompartment)

urlpatterns = [
    path('fmsapi', include(router.urls)),
    path('', admin.site.urls),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='UVGV_FMS/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('UVGV_FMS/api/',include('rest_framework.urls')),
]
