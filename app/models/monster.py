from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.db.models.deletion import CASCADE, PROTECT
from django.conf import settings
from models.stats import Stats



class Monster(models.Model):
   name = models.CharField(max_length=200, null=True)
   descript = models.CharField(max_length=10000, null=True)
   date_created = models.DateTimeField(auto_now_add=True)
   creator = ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT, null=True, default=User)
   stats = ForeignKey(Stats, on_delete=models.PROTECT,null=True)

   def __str__(self) -> str:
       return self.name