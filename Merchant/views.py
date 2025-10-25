from django.shortcuts import render,redirect
from Guest.models import *
from Merchant.models import *
from Plantsman.models import *
from User.models import *


# Create your views here.
def Homepag(request):
    return render(request,'Merchant/Homepage.html')

def myprofile (request):
    sel=tbl_merchant.objects.get(id=request.session['mid'])
    return render(request, 'Merchant/Myprofile.html',{'sel':sel}) 


    
def editprofile (request):
    selec=tbl_merchant.objects.get(id=request.session['mid'])
    if request.method=="POST":
        selec.merchant_name=request.POST.get('txt_name')
        selec. merchant_email=request.POST.get('txt_email')
        selec.merchant_contact=request.POST.get('txt_contact')
        selec.merchant_address=request.POST.get('txt_address')
        selec.save()
        return redirect('Merchant:editprofile')
    else:
         return render(request,'Merchant/Editprofile.html',{'selec':selec})



def changepassword (request):
    merchant=tbl_merchant.objects.get(id=request.session['mid'])
    
    if request.method=="POST":    
       
        
        if(merchant.merchant_password == request.POST.get('txt_oldpassword')):
            if(request.POST.get('txt_newpassword')==request.POST.get('txt_retypepassword')):
                merchant.merchant_password=request.POST.get('txt_newpassword')
                merchant.save()
                return redirect('Merchant:changepassword')
            else:
                return render(request,'Merchant/Changepassword.html',{'msg':'invalid password g'})
        else:
            return render(request,'Merchant/Changepassword.html',{'msg':'invalid password f'})
    else:
            return render(request,'Merchant/Changepassword.html')        



def viewrequest (request):
    plant=tbl_prequest.objects.filter(Merchant=request.session['mid'])
    return render(request,'Merchant/Viewrequest.html',{'plant':plant})

def viewrequestaccept(request,acid):
    reqe=tbl_prequest.objects.get(id=acid) 
    reqe.request_status=1
    reqe.save()
    return redirect("Merchant:viewrequest")


def viewrequestreject(request,reid):
    reqe=tbl_prequest.objects.get(id=reid) 
    reqe.request_status=2
    reqe.save()
    return redirect("Merchant:viewrequest")


def viewrcollect(request,ccid):
    reqe=tbl_prequest.objects.get(id=ccid) 
    reqe.request_status=3
    reqe.save()
    return redirect("Merchant:viewrequest")


def amount(request,id):
    req=tbl_prequest.objects.get(id=id)
    if request.method=="POST":
        req.request_amount=request.POST.get("txt_amount")
        req.save()
        return redirect("Merchant:payment",id)
    else:
        return render(request,'Merchant/Addamount.html')

def payment(request,id):
    preq = tbl_prequest.objects.get(id=id)
#    scrap = tbl_Scrap.objects.get(id=booking.scarp.id)
    amount = preq.request_amount
    if request.method == "POST":
      preq.request_status = 4 
      preq.save()
      return redirect("Merchant:loader")
    else:
      return render(request,"Merchant/Payment.html", {"total":amount})

def loader(request):
    return render(request,"Merchant/Loader.html")

def paymentsuc(request):
    return render(request,"Merchant/Payment_suc.html")




def Addp(request):
    merchant=tbl_merchant.objects.get(id=request.session['mid'])
    mec=tbl_product.objects.all()
    if request.method=="POST":
        name= request.POST.get("txt_name")
        photo=request.FILES.get("txt_photo")
        price=request.POST.get("txt_price")
        discripton=request.POST.get("txt_discription")
        tbl_product.objects.create(product_name=name,product_photo=photo,product_price=price,product_description=discripton,merchant=merchant)
        return redirect('Merchant:Addp')
    else:
        return render(request,'Merchant/Addproduct.html',{'mec':mec})
    

def delproduct(request,pid):
    did=tbl_product.objects.get(id=pid).delete()
    return redirect('Merchant:Addp')
  
def addstock(request,id):
    sto=tbl_addstock.objects.all()
    pro=tbl_product.objects.get(id=id)
    if request.method=="POST":
        stock=request.POST.get("txt_stock")
        tbl_addstock.objects.create(stock_qty=stock,product=pro)
        return redirect('Merchant:Addp')
    else:
        return render(request,'Merchant/Addstock.html',{'sto':sto})
    


def delstock(request,pid):
    did=tbl_addstock.objects.get(id=pid).delete()
    return redirect('Merchant:Addp')


def viewbooking(request):
    book=tbl_cart.objects.filter(product__merchant=request.session['mid'])
    return render(request,'Merchant/Viewbooking.html',{'book':book})

def viewpackage(request,ppid):
    viewbook=tbl_booking.objects.get(id=ppid) 
    viewbook.booking_status=3
    viewbook.save()
    return render(request,'Merchant/Viewbooking.html',{'msg':'packed'})

def shipped(request,shid):
    viewbook=tbl_booking.objects.get(id=shid) 
    viewbook.booking_status=4
    viewbook.save()
    return render(request,'Merchant/Viewbooking.html',{'msg':'shipped'})

def outofdelivered(request,odelid):
    viewbook=tbl_booking.objects.get(id=odelid)
    viewbook.booking_status=5
    viewbook.save()
    return render(request,'Merchant/Viewbooking.html',{'msg':'outofdelivered'})

def delivered(request,delid):
    viewbook=tbl_booking.objects.get(id=delid)
    viewbook.booking_status=6
    viewbook.save()
    return render(request,'Merchant/Viewbooking.html',{'msg':'delivered'})

def viewcomplaint(request):
    comp=tbl_complaint.objects.filter(product__merchant=request.session['mid'])
    return render(request,'Merchant/Viewcomplaint.html',{'comp':comp})

def reply(request,rid):
    rep=tbl_complaint.objects.get(id=rid)

    if request.method=="POST":
        reply=request.POST.get("complaint_reply")
        rep.complaint_reply=reply
        rep.complaint_status=1
        rep.save()
        return redirect('Merchant:viewcomplaint')
    else:
        return render(request,'Merchant/Reply.html')



def logout (request):
    del request.session['mid']
    return redirect("Guest:login")

