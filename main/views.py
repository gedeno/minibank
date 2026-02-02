from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login ,logout ,authenticate
from django.contrib.auth.decorators import login_required
from . models import Users_info
from . forms import form_info
# Create your views here.
def register(request):
    form = UserCreationForm()
    acc_nos = 10005070
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        username = request.POST['username']
        if form.is_valid():
            uss = form.save()
            form1 = Users_info( name = username, acc_no = acc_nos, user = uss)
            form1.save()
            return redirect(f'/login/{uss.id}')
    return render(request,'main/register.html',{'form':form})

def logins(request,uss_id):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password= password)
        if user != None:
            login(request,user)
            return redirect(f'user_ui2/{uss_id}')
    return render(request,'main/login.html')

@login_required(login_url='login')

def user_UI2(request,uss_id):
    if request.method == 'POST':
        user_fill = request.POST.get('user_interest')
        if user_fill == 'deposit':
            return redirect(f'deposits/{uss_id}')
        elif user_fill == 'withdrow':
            return redirect(f'withdrows/{uss_id}')
        elif user_fill == 'balance_checks':
            return redirect(f'balance_checks/{uss_id}')
        elif user_fill == 'transfer':
            return redirect(f'transfers/{uss_id}')
    return render(request,'main/user_ui2.html')

def Deposits(request,usr_id):
    userr = Users_info.objects.get(id=usr_id)
    if request.method == 'POST':
        mony_vals = request.POST.get('mony_val')
        userr.balance += int(mony_vals)
        userr.save()
        return redirect(f'user_ui2/{usr_id}')
    return render(request,'main/deposits.html')