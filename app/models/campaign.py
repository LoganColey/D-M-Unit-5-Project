from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.db.models.deletion import CASCADE, PROTECT
from django.conf import settings


class Campaign(models.Model):
    name = models.CharField(max_length=200)
    descript = models.CharField(max_length=3000)
    date_created = models.DateTimeField(auto_now_add=True)
    creator = ForeignKey(User,on_delete=models.PROTECT, null=True)
