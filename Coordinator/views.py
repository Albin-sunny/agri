from django.shortcuts import render,redirect
from User.models import *
from Coordinator.models import *


# Create your views here.
def Homepa(request):
    return render(request,'Coordinator/Homepage.html')

def myprofile (request):
    sel=tbl_coordinator.objects.get(id=request.session['cid'])
    return render(request, 'Coordinator/Myprofile.html',{'sel':sel})


def editprofile (request):
    sele=tbl_coordinator.objects.get(id=request.session['cid'])
    if request.method=="POST":
        sele.coordinator_name=request.POST.get('txt_name')
        sele.coordinator_email=request.POST.get('txt_email')
        sele.coordinator_contact=request.POST.get('txt_contact')
        sele.coordinator_address=request.POST.get('txt_address')
        sele.save()
        return redirect('Coordinator:editprofile')
    else:
        return render(request,'Coordinator/Editprofile.html',{'sele':sele})


def changepassword (request):
    coordinator=tbl_coordinator.objects.get(id=request.session['cid'])
    
    if request.method=="POST":    
       
        
        if(coordinator.coordinator_password == request.POST.get('txt_oldpassword')):
            if(request.POST.get('txt_newpassword')==request.POST.get('txt_retypepassword')):
                coordinator.coordinator_password=request.POST.get('txt_newpassword')
                coordinator.save()
                return redirect('Coordinator:changepassword')
            else:
                return render(request,'Coordinator/Changepassword.html',{'msg':'invalid password g'})
        else:
            return render(request,'Coordinator/Changepassword.html',{'msg':'invalid password f'})
    else:
        return render(request,'Coordinator/Changepassword.html')        


def plantsman(request):
    coordinator=tbl_coordinator.objects.get(id=request.session['cid'])
    dis=tbl_district.objects.all()
    sel=tbl_plantsman.objects.filter(coordinator=request.session['cid'])
    if request.method=="POST":
        name= request.POST.get("txt_name")
        email= request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        photo=request.FILES.get("txt_photo")
        proof=request.FILES.get("txt_proof")
        loc=tbl_location.objects.get(id=request.POST.get("sel_Location"))
        password=request.POST.get("txt_password")
        tbl_plantsman.objects.create(plantsman_name=name,plantsman_email=email,plantsman_contact=contact,plantsman_address=address,plantsman_photo=photo,plantsman_proof=proof,location=loc,plantsman_password=password,coordinator=coordinator)
        return redirect('Coordinator:plantsman')
    else:
        return render(request,'Coordinator/Plantsman.html',{'dis':dis,'sel':sel})


def delplant(request,did):
    tbl_plantsman.objects.get(id=did).delete()
    return redirect('Coordinator:plantsman')


def viewrequest(request): 
    land=tbl_request.objects.filter(coordinator=request.session['cid'])
    return render(request,'Coordinator/Viewrequest.html',{'land':land})

def viewland(request,id):  
    details=tbl_request.objects.filter(land=id)
    return render(request,'Coordinator/Viewlanddetails.html',{'details':details,'id':id})

def viewrequestaccept(request,acid,lid):
    reqe=tbl_request.objects.get(id=acid) 
    reqe.request_status=1
    reqe.save()
    return render(request,'Coordinator/Viewlanddetails.html',{'id':lid,'msg':"Accepted"})

def vplant(request,lid):
    sel=tbl_plantsman.objects.filter(coordinator=request.session['cid'])
    return render(request,'Coordinator/Viewpantsman.html',{'sel':sel,'lid':lid,})

def assignplant(request,pid,lid):
    plants=tbl_plantsman.objects.get(id=pid)
    land=tbl_land.objects.get(id=lid)
    tbl_assign.objects.create(plantsman=plants,land=land,assign_status=1)
    return render(request,'Coordinator/Viewpantsman.html',{'lid':lid,'msg':"Assigned"})


def reply(request):
    if request.method=="POST":
        reply=request.POST.get("reply")
        tbl_complaint.objects.create(complaint_reply=reply)
        return redirect('Admin:reply')
    
def viewcomplaint(request):
    comp=tbl_complaint.objects.filter(plantsman__coordinator=request.session['cid'])
    return render(request,'Coordinator/Viewcomplaint.html',{'comp':comp})   

def reply(request,rid):
    rep=tbl_complaint.objects.get(id=rid)

    if request.method=="POST":
        reply=request.POST.get("complaint_reply")
        rep.complaint_reply=reply
        rep.complaint_status=1
        rep.save()
        return redirect('Coordinator:viewcomplaint')
    else:
        return render(request,'Coordinator/Reply.html') 
    
def logout (request):
    del request.session['cid']
    return redirect("Guest:login")