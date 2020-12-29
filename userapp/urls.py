from django.urls import *
from . import views

urlpatterns = [
    path('',views.home),
    path('do_sign_up',views.do_sign_up),
    path('do_sign_in',views.do_sign_in),
    path('home',views.home,name='home'),
    path('login_form',views.login_form,name='login'),
    path('signup_form',views.signup_form,name='signup_form'),
    path('cart',views.cart,name='cart'),
    path('otpverify',views.otpverify,name='otpverify'),
]
