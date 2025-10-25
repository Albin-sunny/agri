from django.urls import path,include
from Basics import views
urlpatterns = [
    path('add/',views.add,name="add"),
    path('large/',views.large,name="large"),
   ]