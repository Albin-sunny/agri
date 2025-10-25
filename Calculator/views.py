from django.shortcuts import render

# Create your views here.
def mul(request):
    if request.method == "POST":
        a = request.POST.get("txtn1")
        b = request.POST.get("txtn2")
        c = int(a) + int(b)
        return render(request, 'Calculator/mul.html', {'result': c})
    else:
        return render(request, 'Calculator/mul.html')

    if request.method == "POST":
        a = request.POST.get("txtn1")
        b = request.POST.get("txtn2")
        d = int(a) - int(b)
        return render(request, 'Calculator/mul.html', {'result': d})
    else:
        return render(request, 'Calculator/mul.html')

    if request.method == "POST":
        a = request.POST.get("txtn1")
        b = request.POST.get("txtn2")
        e = int(a) * int(b)
        return render(request, 'Calculator/mul.html', {'result': e})
    else:
        return render(request, 'Calculator/mul.html')

    if request.method == "POST":
        a = request.POST.get("txtn1")
        b = request.POST.get("txtn2")
        f = int(a) / int(b)
        return render(request, 'Calculator/mul.html', {'result': f})
    else:
        return render(request, 'Calculator/mul.html')
