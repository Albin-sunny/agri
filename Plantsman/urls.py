from django.urls import path,include
from Plantsman import views

app_name="Plantsman"
urlpatterns = [

    path('Homepage/',views.homepage,name="homepage"),

    path('myprofile/',views.myprofile,name="myprofile"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path('viewassign/',views.viewassign,name="viewassign"),
    path('viewland/<int:id>',views.viewland,name="viewland"),

    path('Searchmerchant/<int:uid>',views.Searchmerchant,name="Searchmerchant"),


    path('Ajaxplace/',views.ajaxplace,name="ajaxplace"),
   
    path('Ajaxlocation/',views.Ajaxlocation,name="Ajaxlocation"),

    path('AjaxSearch/<int:uid>',views.AjaxSearch, name='AjaxSearch'),

    path('request/<int:mid>/<int:uid>',views.request, name='request'),

    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    # path('ajaxphoto/',views.ajaxphoto,name="ajaxphoto"),
    path('clearchat/',views.clearchat,name="clearchat"),


     path('mrequest/',views.mrequest, name='mrequest'),


    path('amount/<int:id>',views.amount,name="amount"),

    path("payment/<int:id>",views.payment,name="payment"),
    path('loader/',views.loader, name='loader'),
    path('paymentsuc/',views.paymentsuc, name='paymentsuc'),
    path('logout/',views.logout,name="logout"),

]