from django.db import models
from userProfileApp.models import(
    User
)

from companyAsset.models import(
    CompanyAsset
)

# Create your models here.
class EmployeeV(models.Model):
    username = models.CharField(max_length=250, null=True, blank=True)
    asset = models.CharField(max_length=50, blank=True, null=True)
    taking_time = models.DateTimeField(null=True, blank=True)
    back_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.pk}.{self.username}"

