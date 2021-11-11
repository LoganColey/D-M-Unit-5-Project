from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.db.models.deletion import CASCADE, PROTECT
from django.conf import settings

class Stats(models.Model):
    Hp = models.PositiveIntegerField(null=True)
    Str = models.PositiveIntegerField(null=True)
    Dex = models.PositiveIntegerField(null=True)
    Con = models.PositiveIntegerField(null=True)
    Int = models.PositiveIntegerField(null=True)
    Wis = models.PositiveIntegerField(null=True)
    Cha = models.PositiveIntegerField(null=True)
    Walk = models.PositiveIntegerField(null=True)
