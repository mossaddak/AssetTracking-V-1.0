from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from userProfileApp.models import (
    User
)


# Create your views here.
@login_required(login_url='Login')  
def Employee(request):

    if request.user.is_authenticated and request.user.user_type=="Company":
        

        context={
            
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