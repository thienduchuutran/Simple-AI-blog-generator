from django.urls import path
from . import views

urlpatterns = [
    #  blank is for the home page
    path('', views.index, name='index')   
    # how it works? when click on the path, the program will go into view.py file and look for index url

]
