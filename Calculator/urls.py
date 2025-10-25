from django.urls import path,include
from Calculator import views
urlpatterns = [ 
    path('mul/',views.mul, name="mul"),
]
