from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from app.models import KhaoSat, Information
from app.forms import KhaoSatForm
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def dangnhap(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                print("success")
                login(request, user)
                return redirect('khaosat/')
    return render(request, 'app/login.html')

@login_required
def dangxuat(request):
    logout(request)
    return HttpResponse("Bạn đã đăng xuất thành công")

@login_required
def KhaoSatViews(request):
    user = request.user
    check=False
    try:
        user.khaosat
    except ObjectDoesNotExist:
        if request.method == "POST":
            form = KhaoSatForm(data=request.POST)
            if form.is_valid():
                form.save(user)
        else:
            form = KhaoSatForm()
            return render(request, 'app/survey.html', {'form':form, 'check':check})
    else:
        instance = user.khaosat
        form = KhaoSatForm(instance = instance)
        return render(request, 'app/survey.html', {'insert':'Kết quả trả lời khảo sát lần trước', 'form':form})

@login_required
def account(request):
    user = request.user
    fake_information = user.information
    return render(request, 'app/account.html', {'Information':fake_information})
