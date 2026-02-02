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
    return render(request,'main/register.html',{'form':form})

def logins(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password= password)
        if user != None:
            login(request,user)
            return redirect('user_ui')
    return render(request,'main/login.html')
def User_UI(request):
    form = form_info()
    if request.method == 'POST':
        form = form_info(request.POST)
        if form.is_valid:
            usr = form.save(commit=False)
            usr.user = request.user
            usr.save()
            return redirect('user_ui2')
    return render(request,'main/user_ui.html',{'form':form})
@login_required(login_url='login')
def user_UI2(request):
    if request.method == 'POST':
        user_fill = request.POST.get('user_interest')
        if user_fill == 'deposit':
            return redirect('deposits')
        elif user_fill == 'withdrow':
            return redirect('withdrows')
        elif user_fill == 'balance_checks':
            return redirect('balance_checks')
        elif user_fill == 'transfer':
            return redirect('transfers')
    return render(request,'main/user_ui2.html')
