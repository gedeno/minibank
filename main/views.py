from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login ,logout ,authenticate
from django.contrib.auth.decorators import login_required
from . forms import form_info
# Create your views here.
def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('login')
    return render(request,'main/register.html')

def logins(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password= password)
        if user != None:
            login(request,user)
            return redirect()
    return render(request,'main/login.html')

def User_UI(request):
    form = form_info()
    if request.method == 'POST':
        form = form_info(request.POST)
        if form.is_valid:
            usr = form.save(commit=False)
            usr.user = request.user
            usr.save()
            