from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Coordinator.models import *
from Plantsman.models import *
from Merchant.models import *

from django.db.models import Sum
from django.http import JsonResponse
from datetime import datetime
from django.db.models import Q

# Create your views here.
def home (request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
         return render(request, 'User/Homepage.html')
    
def logout (request):
    del request.session['uid']
    return redirect("Guest:login")

def myprofile (request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        sel=tbl_user.objects.get(id=request.session['uid'])
        return render(request, 'user/Myprofile.html',{'sel':sel})
    


def editprofile (request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        sele=tbl_user.objects.get(id=request.session['uid'])
        if request.method=="POST":
            sele.user_name=request.POST.get('txt_name')
            sele.user_email=request.POST.get('txt_email')
            sele.user_contact=request.POST.get('txt_contact')
            sele.user_address=request.POST.get('txt_address')
            sele.save()
            return redirect('User:editprofile')
        else:
            return render(request,'user/Editporifile.html',{'sele':sele})
               


def changepassword (request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        user=tbl_user.objects.get(id=request.session['uid'])
    
        if request.method=="POST":    
       
        
            if(user.user_password == request.POST.get('txt_oldpassword')):
                if(request.POST.get('txt_newpassword')==request.POST.get('txt_retypepassword')):
                    user.user_password=request.POST.get('txt_newpassword')
                    user.save()
                    return redirect('User:changepassword')
                else:
                    return render(request,'User/Changepassword.html',{'msg':'invalid password g'})
            else:
                return render(request,'User/Changepassword.html',{'msg':'invalid password f'})
        else:
            return render(request,'User/Changepassword.html')  
    
          




def complaint (request,pid,id):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        sel = tbl_complaint.objects.filter(user_id=request.session['uid'],product=pid)
        pro=tbl_product.objects.get(id=pid)
        if request.method=="POST":
            complaint_title=request.POST.get('txt_title')
            complaint_content=request.POST.get('txt_content')
            tbl_complaint.objects.create(complaint_title=complaint_title,complaint_content=complaint_content,user_id=tbl_user.objects.get(id=request.session['uid'])
,product=pro)
            return render(request,'User/Complaint.html',{'sel':sel,'pid':pid,'id':id,'msg':"Inserted"})
        else:
            return render(request,'User/Complaint.html',{'sel':sel,'pid':pid,'id':id})
   



def land(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        user=tbl_user.objects.get(id=request.session['uid']) 
        lan=tbl_land.objects.all()
        sel=tbl_land.objects.filter(user=request.session['uid'])
        if request.method=="POST":
            file=request.FILES.get("txt_file")
            details= request.POST.get("txt_landdetails")
            proof=request.FILES.get("txt_proof")
            tbl_land.objects.create(land_file=file,land_details=details,land_proof=proof,user=user)
            return redirect('User:land')
        else:                                                       
            return render(request,'User/Land.html',{'lan':lan,'sel':sel})
      


def delland(request,ldid):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        tbl_land.objects.get(id=ldid).delete()
        return redirect('User:land')
    
 



def Searchcoordinator(request,sid):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        dis = tbl_district.objects.all() 
    # name = request.GET.get("name", "")
    # lid = request.GET.get("lid", "")
    # pid = request.GET.get("pid", "")
    # did = request.GET.get("did", "")

    
    

        ar=[1,2,3,4,5]
        parry=[]
        avg=0
        coordinators = tbl_coordinator.objects.filter(coordinator_status=1)
        for i in coordinators:
            tot=0
            ratecount=tbl_rating.objects.filter(coordinator=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(coordinator=i.id)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            # print(parry)
            datas=zip(coordinators,parry)

        return render(request, "User/Searchcoordinator.html", {"coordinators": datas, "dis": dis,'sid':sid,'ar':ar})
    

def ajaxplace(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        district=tbl_district.objects.get(id=request.GET.get("did"))
        place=tbl_place.objects.filter(district=district)
        return render(request,"User/Ajaxplace.html",{'place':place})

def Ajaxlocation(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        place=tbl_place.objects.get(id=request.GET.get("pid"))  
        locations= tbl_location.objects.filter(place=place)  

    return render(request, "User/AjaxLocation.html", {'locations': locations})

def AjaxSearch(request,sid):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        data=request.GET.get("name")
        land=request.GET.get("lid")
        ar=[1,2,3,4,5]
        parry=[]
        avg=0
    
    
        if data:
            coordinator=tbl_coordinator.objects.filter(coordinator_name__istartswith=data,coordinator_status=1)
            for i in coordinator:
                tot=0
                ratecount=tbl_rating.objects.filter(coordinator=i.id).count()
                if ratecount>0:
                    ratedata=tbl_rating.objects.filter(coordinator=i.id)
                    for j in ratedata:
                        tot=tot+j.rating_data
                        avg=tot//ratecount
                        #print(avg)
                    parry.append(avg)
                else:
                    parry.append(0)
                # print(parry)
                datas=zip(coordinator,parry)
        if land:
            coordinator=tbl_coordinator.objects.filter(location=land,coordinator_status=1)
            for i in coordinator:
                tot=0
                ratecount=tbl_rating.objects.filter(coordinator=i.id).count()
                if ratecount>0:
                    ratedata=tbl_rating.objects.filter(coordinator=i.id)
                    for j in ratedata:
                        tot=tot+j.rating_data
                        avg=tot//ratecount
                        #print(avg)
                    parry.append(avg)
                else:
                    parry.append(0)
            #   print(parry)
                datas=zip(coordinator,parry)
        return render(request, "User/AjaxSearch.html", {'coordinator': datas,'sid':sid,'ar':ar})

   
def request(request,rid,sid):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:    
        land=tbl_land.objects.get(id=sid)
        coor=tbl_coordinator.objects.get(id=rid)
        tbl_request.objects.create(land=land,coordinator=coor)
        return render(request,"User/Searchcoordinator.html",{'sid':sid,'msg':"Requested"})

def viewplant(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
    
        sel=tbl_assign.objects.filter(land__user=request.session['uid'])
 
        return render(request,'User/ViewPlantsman.html',{'sel':sel})


def chatpage(request,id):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        plantsman  = tbl_plantsman.objects.get(id=id)
        return render(request,"User/Chat.html",{"user":plantsman})

def ajaxchat(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        from_user = tbl_user.objects.get(id=request.session["uid"])
        to_plantsman= tbl_plantsman.objects.get(id=request.POST.get("tid"))
        tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,plantsman_to=to_plantsman,chat_file=request.FILES.get("file"))
        return render(request,"User/Chat.html")

def ajaxchatview(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        tid = request.GET.get("tid")
        user = tbl_user.objects.get(id=request.session["uid"])
        chat_data = tbl_chat.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(plantsman_from=tid) | Q(plantsman_to=tid))).order_by('chat_time')
        return render(request,"User/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        tbl_chat.objects.filter(Q(user_from=request.session["uid"]) & Q(plantsman_to=request.GET.get("tid")) | (Q(plantsman_from=request.GET.get("tid")) & Q(user_to=request.session["uid"]))).delete()
        return render(request,"User/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

def vcoordinator(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:

        sel=tbl_request.objects.filter(land__user=request.session['uid'],request_status=1)
        return render(request,'User/ViewCoordinator.html',{'sel':sel})  

  
def vmerchant(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        sel=tbl_prequest.objects.filter(assign__land__user=request.session['uid'],request_status__gte=1)
        return render(request,'User/ViewMerchant.html',{'sel':sel})


def vproduct(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        ar=[1,2,3,4,5]
        parry=[]
        avg=0
        product= tbl_product.objects.all()
        for i in product:
            total_stock = tbl_addstock.objects.filter(product=i.id).aggregate(total=Sum('stock_qty'))['total']
            total_cart = tbl_cart.objects.filter(product=i.id, cart_status=1).aggregate(total=Sum('cart_qty'))['total']
            # print(total_stock)
            # print(total_cart)
            if total_stock is None:
                total_stock = 0
            if total_cart is None:
                total_cart = 0
            total =  total_stock - total_cart
            i.total_stock = total
            tot=0
            ratecount=tbl_rating.objects.filter(product=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(product=i.id)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            # print(parry)
        datas=zip(product,parry)
        return render(request,'User/Viewproduct.html',{'product':datas,'ar':ar})
    


def addtocart(request,id):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        productdata=tbl_product.objects.get(id=id)
        userdata=tbl_user.objects.get(id=request.session["uid"])
        bookingcount=tbl_booking.objects.filter(user=userdata,booking_status=0).count()
        if bookingcount>0:
            bookingdata=tbl_booking.objects.get(user=userdata,booking_status=0)
            cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
            if cartcount>0:
                msg="Already added"
                return render(request,"User/Viewproduct.html",{'msg':msg})
            else:
                tbl_cart.objects.create(booking=bookingdata,product=productdata)
                msg="Added To cart"
                return render(request,"User/Viewproduct.html",{'msg':msg})
        else:
            bookingdata = tbl_booking.objects.create(user=userdata)
            tbl_cart.objects.create(booking=tbl_booking.objects.get(id=bookingdata.id),product=productdata)
            msg="Added To cart"
            return render(request,"User/Viewproduct.html",{'msg':msg})
    
     
def Mycart(request):
    if 'uid' in request.session: 
       
              
        if request.method=="POST":
            bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
            bookingdata.booking_amount=request.POST.get("carttotalamt")
            bookingdata.booking_status=1
            bookingdata.save()
            cart = tbl_cart.objects.filter(booking=bookingdata)
            for i in cart:
                i.cart_status = 1
                i.save()
            return redirect("User:productpayment")
        else:
            bookcount = tbl_booking.objects.filter(user=request.session["uid"],booking_status=0).count()
            if bookcount > 0:
                book = tbl_booking.objects.get(user=request.session["uid"],booking_status=0)
                request.session["bookingid"] = book.id
                cart = tbl_cart.objects.filter(booking=book)
                for i in cart:
                    total_stock = tbl_addstock.objects.filter(product=i.product.id).aggregate(total=Sum('stock_qty'))['total']
                    total_cart = tbl_cart.objects.filter(product=i.product.id, cart_status=0).aggregate(total=Sum('cart_qty'))['total']
                    # print(total_stock)
                    # print(total_cart)
                    if total_stock is None:
                        total_stock = 0
                    if total_cart is None:
                        total_cart = 0
                    total =  total_stock - total_cart
                    i.total_stock = total
                return render(request,"User/MyCart.html",{'cartdata':cart})
            else:
                return render(request,"User/MyCart.html")
    else:
        return redirect("Guest:login")

        

def DelCart(request,did):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        tbl_cart.objects.get(id=did).delete()
        return redirect("User:Mycart")

def CartQty(request):
   if 'uid' not in request.session:
       return redirect("Guest:login")
   else:
        qty=request.GET.get('QTY')
        cartid=request.GET.get('ALT')
        cartdata=tbl_cart.objects.get(id=cartid)
        cartdata.cart_qty=qty
        cartdata.save()
        return redirect("User:Mycart")   

def productpayment(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        bookingdata = tbl_booking.objects.get(id=request.session["bookingid"])
        amt = bookingdata.booking_amount
        if request.method == "POST":
            bookingdata.booking_status = 2
            bookingdata.save()
            return redirect("User:loader")
        else:
            return render(request,"User/Payment.html",{"total":amt})
        
def loader(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        return render(request,"User/Loader.html")

def paymentsuc(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        return render(request,"User/Payment_suc.html")



def mybooking(request):
    if 'uid' not in request.session:
         return redirect("Guest:login")
    else:
        sel=tbl_booking.objects.filter(user=request.session["uid"] ,booking_status__gte=2)
        return render(request,'User/Mybooking.html',{'sel':sel})
    



def viewbooking(request,id):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
            sel=tbl_cart.objects.filter(booking=id)
            return render(request,'User/Viewbookingproduct.html',{'sel':sel,'id':id})
       
def rating(request,mid,name):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        parray=[1,2,3,4,5]
        mid=mid
        # wdata=tbl_booking.objects.get(id=mid)
    
        if name == 1:
            counts=0
            counts=stardata=tbl_rating.objects.filter(product=mid).count()
            if counts>0:
                res=0
                stardata=tbl_rating.objects.filter(product=mid).order_by('-rating_datetime')
                for i in stardata:
                    res=res+i.rating_data
                avg=res//counts
                # print(avg)
                return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts,"name":name})
            else:
                return render(request,"User/Rating.html",{'mid':mid,"name":name})
        elif name == 2:
            counts=0
            counts=stardata=tbl_rating.objects.filter(coordinator=mid).count()
            if counts>0:
                res=0
                stardata=tbl_rating.objects.filter(coordinator=mid).order_by('-rating_datetime')
                for i in stardata:
                    res=res+i.rating_data
                avg=res//counts
            # print(avg)
                return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts,"name":name})
            else:
                return render(request,"User/Rating.html",{'mid':mid,"name":name})
        else:
            return render(request,"User/Rating.html",{'mid':mid,"name":name})

def ajaxstar(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        parray=[1,2,3,4,5]
        rating_data=request.GET.get('rating_data')
        user_name=request.GET.get('user_name')
        rating_review=request.GET.get('rating_review')
        pid=request.GET.get('pid')
        # wdata=tbl_booking.objects.get(id=pid)
        if request.GET.get('name') == '1':
            tbl_rating.objects.create(user=tbl_user.objects.get(id=request.session["uid"]),rating_review=rating_review,rating_data=rating_data,product=tbl_product.objects.get(id=pid))
            stardata=tbl_rating.objects.filter(product=pid).order_by('-rating_datetime')
            return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})
        elif request.GET.get('name') == '2':
            tbl_rating.objects.create(user=tbl_user.objects.get(id=request.session["uid"]),rating_review=rating_review,rating_data=rating_data,coordinator=tbl_coordinator.objects.get(id=pid))
            stardata=tbl_rating.objects.filter(coordinator=pid).order_by('-rating_datetime')
            return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})
        else:
            return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})
    
def starrating(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        r_len = 0
        five = four = three = two = one = 0
        # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    
        if request.GET.get('name') == '1':
            rate = tbl_rating.objects.filter(product=request.GET.get("pdt"))
            ratecount = tbl_rating.objects.filter(product=request.GET.get("pdt")).count()
            for i in rate:
                if int(i.rating_data) == 5:
                    five = five + 1
                elif int(i.rating_data) == 4:
                    four = four + 1
                elif int(i.rating_data) == 3:
                    three = three + 1
                elif int(i.rating_data) == 2:
                    two = two + 1
                elif int(i.rating_data) == 1:
                    one = one + 1
                else:
                    five = four = three = two = one = 0
                # print(i.rating_data)
                # r_len = r_len + int(i.rating_data)
            # rlen = r_len // 5
            # print(rlen)
            result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
            return JsonResponse(result)
        elif request.GET.get('name') == '2':
            rate = tbl_rating.objects.filter(coordinator=request.GET.get("pdt"))
            ratecount = tbl_rating.objects.filter(coordinator=request.GET.get("pdt")).count()
            for i in rate:
                if int(i.rating_data) == 5:
                    five = five + 1
                elif int(i.rating_data) == 4:
                    four = four + 1
                elif int(i.rating_data) == 3:
                    three = three + 1
                elif int(i.rating_data) == 2:
                    two = two + 1
                elif int(i.rating_data) == 1:
                    one = one + 1
                else:
                    five = four = three = two = one = 0
                # print(i.rating_data)
                # r_len = r_len + int(i.rating_data)
            # rlen = r_len // 5
            # print(rlen)
            result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
            return JsonResponse(result)
        else:
            return JsonResponse(result)
   
def pcomplaint (request,iid):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        sel = tbl_complaint.objects.filter(product__isnull=True,user_id=request.session['uid'])
        pla=tbl_plantsman.objects.get(id=iid)
        if request.method=="POST":
            complaint_title=request.POST.get('txt_title')
            complaint_content=request.POST.get('txt_content')
            tbl_complaint.objects.create(complaint_title=complaint_title,complaint_content=complaint_content,user_id=tbl_user.objects.get(id=request.session['uid'])
,           plantsman=pla)
            return render(request,'User/PComplaint.html',{'sel':sel,'msg':"Inserted",'iid':iid})
        else:
                return render(request,'User/PComplaint.html',{'sel':sel,'iid':iid})
    


def feedback(request):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        fed=tbl_feedback.objects.all()
        user=tbl_user.objects.get(id=request.session['uid'])
        if request.method=="POST":
            feedback_content=request.POST.get('txt_content')
            tbl_feedback.objects.create(feedback_content=feedback_content,user=user)
            return redirect("User:feedback") 
        else:
                return render(request,'User/Feedback.html' ,{'fed':fed})    
    
def delfeedback(request,did):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        fed=tbl_feedback.objects.get(id=did)
        fed.delete()
        return redirect("User:feedback")

def delcomplaint(request,cid,pid,id):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        tbl_complaint.objects.get(id=cid).delete()
        return redirect("User:complaint",pid,id)

def delcomp(request,did,iid):
    if 'uid' not in request.session:
        return redirect("Guest:login")
    else:
        tbl_complaint.objects.get(id=did).delete()
        return redirect("User:pcomplaint",iid)      



