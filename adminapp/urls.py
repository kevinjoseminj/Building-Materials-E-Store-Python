from django.urls import *
from . import views

urlpatterns = [
    path('asign_in_form',views.asign_in_form,name='asignin'),
    path('ad_do_sign_in',views.ad_do_sign_in),
    
]



