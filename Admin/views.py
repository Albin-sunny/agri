from django.shortcuts import render,redirect
from django.http import JsonResponse
from Admin.models import *
from Guest.models import *
from Coordinator.models import *
# Create your views here.
def districtinsert(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        district=request.POST.get('txt_District')
        tbl_district.objects.create(district_name=district )
        return render(request,'Admin/District.html',{'dis':dis})
    else:                                                       
        return render(request,'Admin/District.html',{'dis':dis})

def deldistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect('Admin:District')

def editdistrict(request,eid):
    editdata=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        editdata.district_name=request.POST.get("txt_District")
        editdata.save()
        return redirect('Admin:District')
    else:
        return render (request,'Admin/District.html',{'edit':editdata})


    
def adminregistration(request):
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        password=request.POST.get('txt_password')
        tbl_adminregistration.objects.create(admin_name=name,admin_email=email,admin_password=password)
        return render(request,'Admin/AdminRegistration.html')
    else:
        return render(request,'Admin/AdminRegistration.html')

def categoryins(request):
    cate=tbl_category.objects.all()
    if request.method=="POST":
        name=request.POST.get('txt_cat')
        tbl_category.objects.create( category_name=name)
        return render(request,'Admin/category.html',{'cate':cate})
    else:
        return render(request,'Admin/category.html',{'cate':cate})

def delcategory(request,cid):
    tbl_category.objects.get(id=cid).delete()
    return redirect('Admin:category')

def editcategory(request,eid):
    editdata=tbl_category.objects.get(id=eid)
    if request.method=="POST":
        editdata.category_name=request.POST.get("txt_cat")
        editdata.save()
        return redirect('Admin:category')
    else:
        return render(request,'Admin/Category.html',{'edit':editdata})   

        
def placeins(request):
    dis=tbl_district.objects.all()
    place=tbl_place.objects.all()
    if request.method=="POST":
        place=request.POST.get("txt_place")
        district=tbl_district.objects.get(id=request.POST.get("sel_district"))
        tbl_place.objects.create(place_name=place,district=district)
        return redirect('Admin:place')

    else:
        return render(request,'Admin/place.html',{'dis':dis,'place':place})


def delplace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect('Admin:place')

def edplace(request,eid):
    dis=tbl_district.objects.all()
    editdata=tbl_place.objects.get(id=eid)
    if request.method=="POST":
        editdata.district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        editdata.place_name=request.POST.get('txt_place')
        editdata.save()
        return redirect('Admin:place')
    else:
        return render(request,'Admin/Place.html',{'dis':dis,'editdata':editdata})
        
       

def location(request):
    dis=tbl_district.objects.all()
    pla= tbl_place.objects.all()
    locations = tbl_location.objects.all()  #

    if request.method == "POST":
        location_name = request.POST.get("txt_Location")
        place=tbl_place.objects.get(id=request.POST.get("sel_Place"))
        tbl_location.objects.create(location_name=location_name,place=place)

        return redirect('Admin:location')  

    return render(request, 'Admin/Location.html', { 'dis': dis,'pla': pla, 'location': locations})

def dellocation(request, did):
    tbl_location.objects.get(id=did).delete()
    return redirect('Admin:location')

def edlocation(request, eid):
    dis=tbl_district.objects.all()
    pla=tbl_place.objects.all()
    editdata = tbl_location.objects.get(id=eid)

    if request.method == "POST":
        # editdata.district = tbl_district.objects.get(id=request.POST.get('sel_district'))
        # editdata.place = tbl_place.objects.get(id=request.POST.get('sel_Place'))
        editdata.location_name = request.POST.get('txt_Location')
        editdata.save()

        return redirect('Admin:location')

    return render(request, 'Admin/Location.html', {'dis': dis, 'pla': pla, 'editdata': editdata})

    
def subcategoryins(request):
    dis=tbl_subcategory.objects.all()
    cat=tbl_category.objects.all()
    if request.method=="POST":
        subcategory=request.POST.get("txt_sub")
        category=tbl_category.objects.get(id=request.POST.get("sel_cat"))
        tbl_subcategory.objects.create(subcategory_name=subcategory,category=category)
        return render(request,'Admin/Subcategory.html',{'cat':cat,'dis':dis})
    else:
        return render(request,'Admin/Subcategory.html',{'cat':cat,'dis':dis})

        
def delsub(request,caid):
    tbl_subcategory.objects.get(id=caid).delete()
    return redirect('Admin:subcategory')

def esub(request,esid):
    cat=tbl_category.objects.all()
    editdata=tbl_subcategory.objects.get(id=esid)
    if request.method=="POST":
        editdata.category=tbl_category.objects.get(id=request.post.get('sel_cat'))
        editdata.subcategory_name=request.POST.get('txt_sub')
        editdata.save()
        return redirect('Admin:subcategory')    
    else:
        return render(request,'Admin/subcategory.html',{'edit':editdata,'cat':cat})



def Homep (request):
    mer=tbl_merchant.objects.filter(merchant_status=0)
    merchant=tbl_merchant.objects.all().count()
    coordinator=tbl_coordinator.objects.all().count()
    product=tbl_product.objects.all().count()
    return render(request,'Admin/Homepage.html',{'mer':mer,'merchant':merchant,'coordinator':coordinator,'product':product})


def viewcoordinator(request):
    coor=tbl_coordinator.objects.filter(coordinator_status=0)  
    Acceptedcoor=tbl_coordinator.objects.filter(coordinator_status=1)  
    Rejectecoor=tbl_coordinator.objects.filter(coordinator_status=2)
    # coor=tbl_coordinator.objects.filter(coordinator_status=2)  
    return render(request,'Admin/Viewcoordinator.html',{'coor':coor,'Acceptedcoor':Acceptedcoor,'Rejectecoor':Rejectecoor})
    


def viewcoordinatoraccept(request,aid):
    coord=tbl_coordinator.objects.get(id=aid) 
    coord.coordinator_status=1
    coord.save()
    return redirect('Admin:viewcoordinator')

def viewcoordinatorreject(request,rid):
    coordi=tbl_coordinator.objects.get(id=rid) 
    coordi.coordinator_status=2
    coordi.save()
    return redirect('Admin:viewcoordinator')

    
def Ajaxplace(request):
    place=tbl_place.objects.filter(district=request.GET.get("pid"))  
    return render(request, "Admin/Ajaxplace.html", {'place': place})


def viewmerchant(request):
    mer=tbl_merchant.objects.filter(merchant_status=0)
    Acceptedmer=tbl_merchant.objects.filter(merchant_status=1)
    Rejectmer=tbl_merchant.objects.filter(merchant_status=2)
    return render(request,'Admin/Viewmerchant.html',{'mer':mer,'Acceptedmer':Acceptedmer,'Rejectmer':Rejectmer })       

def viewmerchantaccept(request,maid):
    merc=tbl_merchant.objects.get(id=maid) 
    merc.merchant_status=1
    merc.save()
    return redirect('Admin:viewmerchant')

def viewmerchantreject(request,mrid):
    merch=tbl_merchant.objects.get(id=mrid) 
    merch.merchant_status=2
    merch.save()
    return redirect('Admin:viewmerchant')    


def reply(request):
    if request.method=="POST":
        reply=request.POST.get("reply")
        tbl_complaint.objects.create(complaint_reply=reply)
        return redirect('Admin:reply')
    

def  viewfeedback(request):
    feed=tbl_feedback.objects.all()
    return render(request,'Admin/Viewfeedback.html',{'feed':feed}) 

def delfeedback(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect('Admin:viewfeedback')
def logout (request):
    del request.session['aid']
    return redirect("Guest:login")