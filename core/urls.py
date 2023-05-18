from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #manin
    path('', include('main.urls')),

    #user profile
    path('', include('userProfileApp.urls')),

    #company asset
    path('', include('companyAsset.urls')),

    #employee
    path('', include('employee.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
