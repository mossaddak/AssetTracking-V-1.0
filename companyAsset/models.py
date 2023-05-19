from django.db import models
from userProfileApp.models import (
    User
)

# Create your models here.
class CompanyAsset(models.Model):
    user = models.ForeignKey(User, related_name="CompanyAssetUserRelatedname", on_delete=models.CASCADE, null=True, blank=False)
    name = models.CharField(max_length=50, null=True, blank=False)
    employee_list = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f"{self.pk}.{self.name}"
