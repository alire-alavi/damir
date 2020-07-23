from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

from .validators import validate_phone_number

class CostumerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=32, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    phone = models.CharField(max_length=15 , validators=[validate_phone_number], null=True, blank=True)
    office_phone_number = models.CharField(max_length=15 , validators=[validate_phone_number], null=True, blank=True)
    company_name = models.CharField(max_length=64, null=True, blank=True)
    company_address = models.CharField(_("آدرس شرکت"), max_length=500, null=True, blank=True)
    office_address = models.CharField(_("آدرس دفتر"), max_length=500, null=True, blank=True)
    province = models.CharField(_("استان"), max_length=50, null=True, blank=True)
    city = models.CharField(_("شهر"), max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.username



class ProducerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=32, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    phone = models.CharField(max_length=15 , validators=[validate_phone_number], null=True, blank=True)
    office_phone_number = models.CharField(max_length=15 , validators=[validate_phone_number], null=True, blank=True)
    company_name = models.CharField(max_length=64, null=True, blank=True)
    company_address = models.CharField(_("آدرس شرکت"), max_length=500, null=True, blank=True)
    office_address = models.CharField(_("آدرس دفتر"), max_length=500, null=True, blank=True)
    province = models.CharField(_("استان"), max_length=50, null=True, blank=True)
    city = models.CharField(_("شهر"), max_length=50, null=True, blank=True)
    category = models.ManyToManyField(Category, verbose_name=_("دسته بندی"))

    def __str__(self):
        return self.user.username




    