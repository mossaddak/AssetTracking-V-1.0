from django.shortcuts import render
from userProfileApp.models import (
    User
)
from django.contrib import messages
from django.http import HttpResponseRedirect
from employee.models import(
    EmployeeV
)

# Create your views here.

def Home(request):

    if request.user.is_authenticated and request.user.user_type=="Company":
        user = User.objects.get(username=request.user.username)
        employees = user.employee.all()     

        context={
            "employees":employees,
            "allAsset":request.user.CompanyAssetUserRelatedname.all(),
            #"employee_taken_asset":EmployeeV.objects.filter(username=employee.username)
        }
    else:
        
        context = {

        }
    return render(request, 'home.html', context = context)

def AssingAsset(request, pk):

    

    user = User.objects.get(pk=pk)
    print("User===================================>", user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))