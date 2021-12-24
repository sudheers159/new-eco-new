from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from app.models import Contact, register_table
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    recent=Contact.objects.all()[:6]
    return render(request, 'index.html',{'messege':recent})


def contact(request):
    all_data=Contact.objects.all()
    
    
    if request.method=='POST':
        name=request.POST['name']
        contact=request.POST['contact']
        subject=request.POST['subject']
        msg=request.POST['message']

        # return HttpResponse("<h1>"+name+"</h1>")

        aa=Contact(name=name, contact=contact, subject=subject, msg=msg)
        aa.save()
        return HttpResponse("<h1>Data Saved Successfully</h1>")

    return render(request, "contact.html",{'aa':all_data})


def category_new(request):
    return render(request, 'category.html')

def register(request):
    if request.method=='POST':
        fname=request.POST['first']
        lname=request.POST['last']
        un=request.POST['uname']
        pwd=request.POST['password']
        em=request.POST['email']
        con=request.POST['contact']
        tp=request.POST['utype']
        # print(request.POST)
        usr=User.objects.create_user(un,em, pwd)
        usr.first_name=fname
        usr.last_name=lname  
        if tp=='sell':
            usr.is_staff=True
        usr.save()

        reg=register_table(user=usr,contact=con)
        
        reg.save()
        return render( request , 'register.html',{"status":f"{fname} Registerd Successfully"})
       


    return render(request , 'register.html')

def check_user(request):
    if request.method=="GET":
        un=request.GET["usern"]
        check=User.objects.filter(username=un)
        print(check,len(check))
        if len(check)== 1:
            return HttpResponse("Exits")
        else:

            return HttpResponse("not Exist")
    

# @login_required   
def user_login(request):
    if request.method=="POST":
        un=request.POST["username"]
        pwd=request.POST["password"]
        user=authenticate(username=un, password=pwd)
        if user:
            login(request,user)
            if user.is_superuser:
                return HttpResponseRedirect("/admin") 
            if user.is_staff:
                # return render(request, "customer.html")
                return HttpResponseRedirect("/seller")
            if user.is_active:
                # return render(request, "sellerdashboard.html")
                return HttpResponseRedirect("/customer")
        else:
            return render(request,"index.html" ,{"status":"invalid user password"})

        return HttpResponse(user)

    print("hello Login")
    return HttpResponse("Called")

# @login_required   
def customer(request):
    return render(request, "customer.html")    

# @login_required   
def seller(request):
    return render(request, "sellerdashboard.html")    

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/home')



   