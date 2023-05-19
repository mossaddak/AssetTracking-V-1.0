from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from userProfileApp.models import (
    User
)
from companyAsset.models import (
    CompanyAsset
)
from .models import(
    EmployeeV
)


# Create your views here.
@login_required(login_url='Login')  
def Employee(request):

    if request.user.is_authenticated and request.user.user_type=="Company":
        user = User.objects.get(username=request.user.username)
        employees = user.employee.all()
            

        context={
            "employees":employees
        }
    else:
        messages.warning(request, "you don't have permission for this page.")
        context = {

        }

    return render(request, 'employee.html', context=context)


@login_required(login_url='Login')
def AddEmployee(request):
    if request.user.is_authenticated and request.user.user_type=="Company":
        try:
            employee_search = request.GET.get('employee')
            employee = User.objects.get(username=employee_search)

            if employee.user_type != "Company" :
                user = User.objects.get(username=request.user.username)
                user.employee.add(employee)

                

                user.save()
                messages.success(request, f"{employee.username} successfully added") 
            else:
                messages.warning(request, f"no employee is found with this username") 
        
        except Exception as e:
            messages.warning(request, f"{e}") 
    else:
        messages.warning(request, "you don't have permission for this page.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='Login')
def EmployeeProfile(request, pk):
    try:
        employee = get_object_or_404(User,pk=pk)
        search_asset = request.POST.get('asset_item')
        allAsset = request.user.CompanyAssetUserRelatedname.all()
        print(employee.username)
        is_employee_taken = EmployeeV.objects.filter(username=employee.username, asset=search_asset)

        print("iS========================================>", is_employee_taken)

        if not is_employee_taken:
            if search_asset:                                                                                    
                asset = allAsset.get(name=search_asset)
                if asset:
                    asset.employee_list.add(employee)
                    EmployeeV.objects.create(
                        username=employee.username,
                        asset=asset
                    )
                    messages.success(request, "successfully asset shared")
                else:
                    messages.warning(request, "don't have any asset with this name")
        else:
            messages.warning(request, "this user already have this device")
        
        if request.user in employee.employee.all():
            context = {
                "employee":employee,
                "allAsset":allAsset
            }
        else:
            context = {
                
            }
    
        return render (request,'employee_profile.html', context)
    except:
        return render (request,'employee_profile.html')
