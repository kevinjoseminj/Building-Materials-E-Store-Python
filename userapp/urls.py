from django.urls import *
from . import views

urlpatterns = [
    path('',views.home),
    path('home',views.home,name='home'),
    path('login_form',views.login_form,name='login'),
    path('signup_form',views.signup_form,name='signup_form'),
    path('cart',views.cart,name='cart'),

    #path('logout/',views.logout),
]
