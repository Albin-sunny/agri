from django.shortcuts import render

# Create your views here.

def add(request):
        if request.method=="POST":
            a=request.POST.get("Number1")
            b=request.POST.get("Number2")
            c=int(a)+int(b)
            return render(request,'Basics/Add.html',{'result':c})
        else:
            return render(request,'Basics/Add.html')


def large(request):
    if request.method=="POST":
        a=request.POST.get("txt_number1")
        b=request.POST.get("txt_number2")
        if(a>b):
            return render(request,'Basics/Large.html',{'result':a})
        else:
            return render(request,'Basics/Large.html',{'result':b})
    else:
        return render(request,'Basics/Large.html')
            

