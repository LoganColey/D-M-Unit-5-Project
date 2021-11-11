from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.db.models.deletion import CASCADE, PROTECT
from django.conf import settings
from models.campaign import Campaign


class Notes(models.Model):
    descript = models.CharField(max_length=3000)
    campaign = ForeignKey(Campaign,on_delete=models.PROTECT, null=True)
