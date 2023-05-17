from django.shortcuts import render, redirect
from .models import(
    CompanyAsset
)
from django.http import HttpResponseRedirect
from django.contrib import messages
from userProfileApp.models import(
    User
)


# Create your views here.
def AddAsset(request):
    user = User.objects.get(username=request.user.username)
    company_assets = user.CompanyAssetUserRelatedname.all()
    print("AllAsset======================================>", company_assets)
    name = request.GET.get("asset_name")
    is_asset_present = company_assets.filter(name=name)

    if request.user.is_authenticated:

        if not is_asset_present:

            if request.method=="GET" and request.user.user_type == "Company":
                blog1 = CompanyAsset.objects.create(
                    user=request.user,
                    name=name
                )
                blog1.save()
                messages.success(request,f"{name} successfully added.")
            else:
                messages.warning(request,f"You don't have permission for this action")
        else:
            messages.warning(request,f"{name} Allready present")
    else:
        messages.warning(request,f"please log into your account.")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 