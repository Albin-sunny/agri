from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Coordinator.models import *






# Create your views here.
def user(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        name= request.POST.get("txt_name")
        email= request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        photo=request.FILES.get("txt_photo")
        loc=tbl_location.objects.get(id=request.POST.get("sel_location"))
        password=request.POST.get("txt_password")
        tbl_user.objects.create(user_name=name,user_email=email,user_contact=contact,user_address=address,user_photo=photo,location=loc,user_password=password)
        return redirect('Guest:user')
    else:
        return render(request,'Guest/Userregistration.html',{'dis':dis})

def ajaxplace(request):
    district=tbl_district.objects.get(id=request.GET.get("did"))
    place=tbl_place.objects.filter(district=district)
    return render(request,"Guest/Ajaxplace.html",{'place':place})

def Ajaxlocation(request):
    place=tbl_place.objects.get(id=request.GET.get("pid"))  
    locations= tbl_location.objects.filter(place=place)  
    return render(request, "Guest/AjaxLocation.html", {'locations': locations})


def login(request):
    if request.method=="POST":
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        admincount=tbl_adminregistration.objects.filter(admin_email=email,admin_password=password).count()
        coordinatorcount=tbl_coordinator.objects.filter(coordinator_email=email,coordinator_password=password,).count()
        merchantcount=tbl_merchant.objects.filter(merchant_email=email,merchant_password=password).count()
        plantsmancount=tbl_plantsman.objects.filter(plantsman_email=email,plantsman_password=password).count()
        if usercount >0:
            user=tbl_user.objects.get(user_email=email,user_password=password)
            request.session['uid']=user.id
            user.save()
            return redirect("User:home")

        elif coordinatorcount >0:
            coordinator=tbl_coordinator.objects.get(coordinator_email=email,coordinator_password=password,coordinator_status='1')
            request.session['cid']=coordinator.id
            coordinator.save()
            return redirect("Coordinator:Homepa")


        elif merchantcount >0:
            merchant=tbl_merchant.objects.get(merchant_email=email,merchant_password=password,merchant_status='1')
            request.session['mid']=merchant.id
            merchant.save()
            return redirect("Merchant:Homepag")  

        elif plantsmancount >0:
            plantsman=tbl_plantsman.objects.get(plantsman_email=email,plantsman_password=password)
            request.session['plid']=plantsman.id
            plantsman.save()
            return redirect("Plantsman:homepage")        

        elif admincount>0:
            admin=tbl_adminregistration.objects.get(admin_email=email,admin_password=password)
            request.session['aid']=admin.id
            admin.save()
            return redirect("Admin:Homep")
        else:
            return render(request,"Guest/Login.html",{'msg':'Invalid Email or Password'})
    else:
        return render(request,"Guest/Login.html")

    
        


def coordinator(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        name= request.POST.get("txt_name")
        email= request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        photo=request.FILES.get("txt_photo")
        proof=request.FILES.get("txt_proof")
        
        loc=tbl_location.objects.get(id=request.POST.get("sel_Location"))
        password=request.POST.get("txt_password")
        tbl_coordinator.objects.create(coordinator_name=name,coordinator_email=email,coordinator_contact=contact,coordinator_address=address,coordinator_photo=photo,coordinator_proof=proof,location=loc,coordinator_password=password)
        return redirect('Guest:coordinator')
    else:
        return render(request,'Guest/Coordinator.html',{'dis':dis})



def merchant(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        name= request.POST.get("txt_name")
        email= request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        photo=request.FILES.get("txt_photo")
        proof=request.FILES.get("txt_proof")
        loc=tbl_location.objects.get(id=request.POST.get("sel_Location"))
        password=request.POST.get("txt_password")
        tbl_merchant.objects.create(merchant_name=name,merchant_email=email,merchant_contact=contact,merchant_address=address,merchant_photo=photo,merchant_proof=proof,location=loc,merchant_password=password)
        return redirect('Guest:merchant')
    else:
        return render(request,'Guest/Merchant.html',{'dis':dis})




def index(request):
    return render(request,'Guest/index.html')