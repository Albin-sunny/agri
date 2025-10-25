from django.urls import path
from Guest import views
app_name="Guest"
urlpatterns = [
    path('user/',views.user,name="user"),
    path('coordinator/',views.coordinator,name="coordinator"),
    path('Merchant/',views.merchant,name="merchant"),
    path('Ajaxplace/',views.ajaxplace,name="ajaxplace"),
    path('Ajaxlocation/',views.Ajaxlocation,name="Ajaxlocation"),
    path('Login/',views.login,name="login"),
    path('',views.index,name="index"),
   
    
]