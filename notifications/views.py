from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):
    return render(request,'notifications/login.html')

def resetpassword(request):
    return render(request,'notifications/resetpassword.html')

def dashboard(request):
    return render(request,'notifications/dashboard.html')
def dashboardTenants(request):
    return render(request,'notifications/tenantslist.html')
