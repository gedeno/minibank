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
            return redirect('login')
    return render(request,'main/register.html',{'form':form})

def logins(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password= password)
        if user != None:
            login(request,user)
            return redirect('deposite_name')
    return render(request,'main/login.html')

@login_required(login_url='login')
def deposite_name(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        userr = Users_info.objects.get(name=name)
        if userr:
            return redirect(f'/user_ui2/{userr.id}')
    return render(request,'main/deposite_name.html')



def user_UI2(request,id):
    if request.method == 'POST':
        user_fill = request.POST.get('user_interest')
        if user_fill == 'deposit':
            return redirect(f'/deposits/{id}')
        elif user_fill == 'withdrow':
            return redirect(f'/withdrows/{id}')
        elif user_fill == 'balance_checks':
            return redirect(f'/balance_checks/{id}')
        elif user_fill == 'transfer':
            return redirect(f'/transfers/{id}')
    return render(request,'main/user_ui2.html')


def Deposits(request,id):
    userr = Users_info.objects.get(id=id)
    if request.method == 'POST':
        mony_vals = request.POST.get('mony_val')
        userr.balance =userr.balance + int(mony_vals)
        userr.save()
        return redirect(f'/user_ui2/{id}')
    return render(request,'main/deposit.html')


def withdrows(request,id):
    userr = Users_info.objects.get(id = id)
    if request.method == 'POST':
        mony_vals = request.POST.get('mony_val')
        if userr.balance >= int(mony_vals):
            userr.balance = userr.balance - int(mony_vals)
            userr.save()
            return redirect(f'/user_ui2/{id}')
    return render(request,'main/withdrow.html')
