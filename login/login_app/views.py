from django.shortcuts import render
from django.shortcuts import redirect, HttpResponseRedirect
from .models import signup
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == 'POST':
        member = signup(username=request.POST['username'], password=request.POST['password'],  email=request.POST['email'])
        member.save()
        messages.success(request,"Registered Successfully!!!")
        return redirect('/')
        
    else:
        return render(request, 'index.html')
 
def login(request):
    return render(request, 'login.html')
 
def home(request):
    if request.method == 'POST':
        if signup.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = signup.objects.get(username=request.POST['username'], password=request.POST['password'])
            messages.success(request,"Login Successfully!!!")
            return render(request, 'home.html', {'member': member})
        else:
            messages.error(request,"Invalid Username Or Password.")
            return render(request, 'login.html')
