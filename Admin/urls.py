from django.urls import path
from Admin import views
app_name="Admin"
urlpatterns = [
    path('District/',views.districtinsert,name="District"),
    path('deldistrict/<int:did>',views.deldistrict,name="deldistrict"),
    path('editdistrict/<int:eid>',views.editdistrict,name="editdistrict"),


    path('adminregistration/',views.adminregistration,name="AdminRegistation"),

    path('category/',views.categoryins,name="category"),
    path('delcategory/<int:cid>',views.delcategory,name="delcategory"),
    path('editcategory/<int:eid>',views.editcategory,name="editcategory"),

    path('place/',views.placeins,name="place"),
    path('delplace/<int:did>',views.delplace,name="delplace"),   
    path('edplace/<int:eid>',views.edplace,name="edplace"),

    path('location/',views.location,name="location"),
    path('dellocation/<int:did>',views.dellocation,name="dellocation"),
    path('edlocation/<int:eid>',views.edlocation,name="edlocation"),
    path('Ajaxplace/',views.Ajaxplace,name="Ajaxplace"),


    path('subcategory/',views.subcategoryins,name="subcategory"),
    path('delsub/<int:caid>',views.delsub,name="delsub"),
    path('esub/<int:esid>',views.esub,name="esub"),

    path ('Homep/',views.Homep,name="Homep"),

    path ('viewcoordinator/',views.viewcoordinator,name="viewcoordinator"),
    path('viewcoordinatoraccept/<int:aid>',views.viewcoordinatoraccept,name="viewcoordinatoraccept"),
    path('viewcoordinatorreject/<int:rid>',views.viewcoordinatorreject,name="viewcoordinatorreject"),



    path('viewmerchant/',views.viewmerchant,name="viewmerchant"),
    path('viewmerchantaccept/<int:maid>',views.viewmerchantaccept,name="viewmerchantaccept"),
    path('viewmerchantreject/<int:mrid>',views.viewmerchantreject,name="viewmerchantreject"),
    path('reply/',views.reply,name="reply"),
     path('viewfeedback/',views.viewfeedback,name="viewfeedback"),
     path('delfeedback/<int:did>',views.delfeedback,name="delfeedback"),
     path('logout/',views.logout,name="logout"),        

     
    
]