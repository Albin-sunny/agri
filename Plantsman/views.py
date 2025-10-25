from django.shortcuts import render,redirect
from Guest.models import *
from Coordinator.models import *
from Plantsman.models import *
from datetime import datetime

from django.db.models import Q
# Create your views here.
def homepage(request):
    return render(request, 'plantsman/Homepage.html')



def myprofile (request):
    sel=tbl_plantsman.objects.get(id=request.session['plid'])
    return render(request,'plantsman/Myprofile.html',{'sel':sel})    


def editprofile (request):
    sele=tbl_plantsman.objects.get(id=request.session['plid'])
    if request.method=="POST":
        sele.plantsman_name=request.POST.get('txt_name')
        sele.plantsman_email=request.POST.get('txt_email')
        sele.plantsman_contact=request.POST.get('txt_contact')
        sele.plantsman_address=request.POST.get('txt_address')
        sele.save()
        return redirect('Plantsman:editprofile')
    else:
         return render(request,'plantsman/Editprofile.html',{'sele':sele})  

 
       
def changepassword (request):
    plantsman=tbl_plantsman.objects.get(id=request.session['plid'])
    if request.method=="POST":            
        if(plantsman.plantsman_password == request.POST.get('txt_oldpassword')):
            if(request.POST.get('txt_newpassword')==request.POST.get('txt_retypepassword')):
                plantsman.plantsman_password=request.POST.get('txt_newpassword')
                plantsman.save()
                return redirect('Plantsman:changepassword')
            else:
                return render(request,'plantsman/Changepassword.html',{'msg':'invalid password g'})
        else:
            return render(request,'plantsman/Changepassword.html',{'msg':'invalid password f'})
    else:
            return render(request,'plantsman/Changepassword.html')        

def viewassign(request):
    land=tbl_assign.objects.filter(plantsman=request.session['plid'])
    return render(request,'Plantsman/Viewassignwork.html',{'land':land})


def viewland(request,id):  
    detail=tbl_assign.objects.filter(land=id)
    return render(request,'Plantsman/Viewland.html',{'detail':detail,'id':id})





def Searchmerchant(request,uid):
    dis=tbl_district.objects.all()
    merchants=tbl_merchant.objects.filter(merchant_status=1)
    return render(request, "Plantsman/Searchmerchant.html", {"merchants": merchants,"dis": dis,'uid':uid})

def ajaxplace(request):
    district=tbl_district.objects.get(id=request.GET.get("did"))
    place=tbl_place.objects.filter(district=district)
    return render(request,"Plantsman/Ajaxplace.html",{'place':place})

def Ajaxlocation(request):
    place=tbl_place.objects.get(id=request.GET.get("pid"))  
    locations= tbl_location.objects.filter(place=place)  

    return render(request, "Plantsman/AjaxLocation.html", {'locations': locations})

def AjaxSearch(request,uid):
    data=request.GET.get("name")
    location=request.GET.get("lid")
    if data:
        merchant=tbl_merchant.objects.filter(merchant_name__istartswith=data,merchant_status=1)
    if location:
        merchant=tbl_merchant.objects.filter(location=location)
    return render(request, "Plantsman/AjaxSearch.html",{'merchants':merchant,'uid':uid})



def request(request,mid,uid):
    # plantsman=tbl_plantsman.objects.get(id=request.session['plid'])
    merchant=tbl_merchant.objects.get(id=mid)
    assign=tbl_assign.objects.get(id=uid)
    if request.method=="POST":
        discription= request.POST.get("txt_desc")
        tbl_prequest.objects.create(Merchant=merchant,discription=discription,assign=assign)
        return render(request,"Plantsman/Searchmerchant.html",{'mid':mid,'msg':"requested",'uid':uid})
    else:
        return render(request,"Plantsman/prequest.html",{'mid':mid})

def chatpage(request,id):
    user  = tbl_user.objects.get(id=id)
    return render(request,"Plantsman/Chat.html",{"user":user})

def ajaxchat(request):
    from_plantsman = tbl_plantsman.objects.get(id=request.session["plid"])
    to_user = tbl_user.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),plantsman_from=from_plantsman,user_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"Plantsman/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    plantsman = tbl_plantsman.objects.get(id=request.session["plid"])
    chat_data = tbl_chat.objects.filter((Q(plantsman_from=plantsman) | Q(plantsman_to=plantsman)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"Plantsman/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(plantsman_from=request.session["plid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(plantsman_to=request.session["plid"]))).delete()
    return render(request,"Plantsman/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

def mrequest(request):
    sel=tbl_prequest.objects.filter( assign__plantsman=request.session['plid'],request_status__gte=1)
    return render(request,'Plantsman/MyRequest.html',{'sel':sel})  




def amount(request,id):
    req=tbl_prequest.objects.get(id=id)
    if request.method=="POST":
        req.User_amount=request.POST.get("txt_amount")
        req.save()
        return redirect("Plantsman:payment",id)
    else:
        return render(request,'Plantsman/Addamount.html')

def payment(request,id):
    preq = tbl_prequest.objects.get(id=id)
#    scrap = tbl_Scrap.objects.get(id=booking.scarp.id)
    amount = preq.User_amount
    if request.method == "POST":
      preq.request_status = 5 
     
      preq.save()
      return redirect("Plantsman:loader")
    else:
      return render(request,"Plantsman/Userpayment.html", {"total":amount})

def loader(request):
    return render(request,"Plantsman/Loader.html")

def paymentsuc(request):
    return render(request,"Plantsman/Payment_suc.html")

def logout (request):
    del request.session['plid']
    return redirect("Guest:login")
