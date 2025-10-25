from django.urls import path
from Coordinator import views

app_name="Coordinator"
urlpatterns = [
    path ('Homepa/',views.Homepa,name="Homepa"),
    path('myprofile/',views.myprofile,name="myprofile"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path('plantsman/',views.plantsman,name="plantsman"),
    path('delplant/<int:did>',views.delplant,name="delplant"),
    

    path('viewrequest/',views.viewrequest,name="viewrequest"),

    path('viewland/<int:id>',views.viewland,name="viewland"),

    path('viewrequestaccept/<int:acid>/<int:lid>',views.viewrequestaccept,name="viewrequestaccept"),
    

     path('vplant/<int:lid>',views.vplant,name="vplant"),
     path('assignplant/<int:pid>/<int:lid>',views.assignplant,name="assignplant"),
      path('reply/',views.reply,name="reply"),
    path('viewcomplaint/',views.viewcomplaint,name="viewcomplaint"),
    path('reply/<int:rid>',views.reply,name="reply"),
    path('logout/',views.logout,name="logout"),
    

    ]              