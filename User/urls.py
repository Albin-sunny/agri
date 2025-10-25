from django.urls import path,include
from User import views
app_name="User"
urlpatterns = [
   path('Homepage/',views.home,name="home"),
   path('myprofile/',views.myprofile,name="myprofile"),
   path('editprofile/',views.editprofile,name="editprofile"),
   path('changepassword/',views.changepassword,name="changepassword"),

   path('complaint/<int:pid>/<int:id>',views.complaint,name="complaint"),
   path('delcomplaint/<int:cid>/<int:pid>/<int:id>',views.delcomplaint,name="delcomplaint"),


   path('land/',views.land,name="land"),
   path('delland/<int:ldid>',views.delland,name="delland"),

   path ('Searchcoordinator/<int:sid>',views.Searchcoordinator,name="Searchcoordinator"),
   path('Ajaxplace/',views.ajaxplace,name="ajaxplace"),
   
   path('Ajaxlocation/',views.Ajaxlocation,name="Ajaxlocation"),

   path('ajaxsearch/<int:sid>', views.AjaxSearch, name='AjaxSearch'),

   path('request/<int:rid>/<int:sid>',views.request, name='request'),
   path('viewplant/',views.viewplant,name="viewplant"),

   path('chatpage/<int:id>',views.chatpage,name="chatpage"),
   path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
   path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    # path('ajaxphoto/',views.ajaxphoto,name="ajaxphoto"),
   path('clearchat/',views.clearchat,name="clearchat"),

    path('vcoordinator/',views.vcoordinator,name="vcoordinator"),
    path('vmerchant/',views.vmerchant,name="vmerchant"),

     path('vproduct/',views.vproduct,name="vproduct"),

    path('addtocart/<int:id>',views.addtocart,name="addtocart"),

    path('Mycart/',views.Mycart, name='Mycart'),   
    path("DelCart/<int:did>", views.DelCart,name="delcart"),
    path("CartQty/", views.CartQty,name="cartqty"),

    path("productpayment/", views.productpayment,name="productpayment"),
    path('loader/',views.loader, name='loader'),
    path('paymentsuc/',views.paymentsuc, name='paymentsuc'),

    path('mybooking/',views.mybooking,name="mybooking"),


   path('viewbooking/<int:id>',views.viewbooking,name="viewbooking"),

   path('rating/<int:mid>/<int:name>',views.rating,name="rating"),  
   path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
   path('starrating/',views.starrating,name="starrating"),
   path('pcomplaint/<int:iid>',views.pcomplaint,name="pcomplaint"),
   path('feedback/',views.feedback,name="feedback"),
   path('delfeedback/<int:did>',views.delfeedback,name="delfeedback"),
   path('delcomp/<int:did>/<int:iid>',views.delcomp,name="delcomp"),
   path('logout/',views.logout,name="logout"),

   
   
   

]