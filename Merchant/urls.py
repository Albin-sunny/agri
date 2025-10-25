from django.urls import path
from Merchant import views
app_name="Merchant"
urlpatterns = [
    
    path ('Homepag/',views.Homepag,name="Homepag"),
    path('myprofile/',views.myprofile,name="myprofile"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('viewrequest/',views.viewrequest,name="viewrequest"),
    path('viewrequestaccept/ <int:acid>/',views.viewrequestaccept,name="viewrequestaccept"),
    path('viewrequestreject/ <int:reid>/',views.viewrequestreject,name="viewrequestreject"),
    path('viewrcollect/ <int:ccid>/',views.viewrcollect,name="viewrcollect"),

     path('amount/<int:id>',views.amount,name="amount"),

     path("payment/<int:id>",views.payment,name="payment"),
    path('loader/',views.loader, name='loader'),
    path('paymentsuc/',views.paymentsuc, name='paymentsuc'),

    path('Addp/',views.Addp,name="Addp"),

    path('delproduct/<int:pid>',views.delproduct,name="delproduct"),


    path('addstock/<int:id>/',views.addstock,name="addstock"),
    path('delstock/<int:pid>/',views.delstock,name="delstock"),

    path('viewbooking/',views.viewbooking,name="viewbooking"),


     path('viewpackage/<int:ppid>',views.viewpackage,name="viewpackage"),

    path('shipped/<int:shid>',views.shipped,name="shipped"),

    path('delivered/<int:delid>',views.delivered,name="delivered"),

    path('outofdelivered/<int:odelid>',views.outofdelivered,name="outofdelivered"),


    path('viewcomplaint/',views.viewcomplaint,name="viewcomplaint"),
     path('reply/<int:rid>',views.reply,name="reply"),
     path('logout/',views.logout,name="logout"),
     

]