from django.urls import *
from . import views

urlpatterns = [
    path('',views.home),
    #path('', TemplateView.as_view(template_name='blog.html')),
    #path('loginlog/',views.loginlog),
    #path('logout/',views.logout),
]
