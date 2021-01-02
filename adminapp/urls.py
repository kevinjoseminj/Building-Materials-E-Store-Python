from django.urls import *
from . import views

urlpatterns = [
    path('asign_in_form',views.asign_in_form,name='asignin'),
    path('ad_do_sign_in',views.ad_do_sign_in),
    path('products',views.products,name='products'),
    path('viewproducts',views.viewproducts,name='viewproducts'),
    path('addproducts',views.addproducts,name='addproducts'),
    path('viewdelete',views.viewdelete,name='viewdelete'),
    path('saveproducts',views.saveproducts,name='saveproducts'),
    path('editproduct/<int:id>',views.editproduct,name='editproduct'),
    path('updateproduct/<int:id>',views.updateproduct,name='updateproduct'),
    path('deleteproduct/<int:id>',views.deleteproduct,name='deleteproduct'),
    path('orderlist',views.orderlist,name='orderlist'),
    path('confirm',views.confirm,name='confirm'),

    
]



