from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    c = ''
    if request.method == "POST":
        n1 = float(request.POST.get('num1'))
        n2 = float(request.POST.get('num2'))
        oper = request.POST.get('optr')
        if oper == "+":
            c=n1+n2
        elif oper=="-":
            c=n1-n2
        elif oper=="*":
            c=n1*n2
        elif oper == "/":
            if n2==0:
                c="ERROR..."
            else:
                c=n1/n2
        else:
            return HttpResponse("Invalid")

    return render(request,"calculator.html",{'c': c})









