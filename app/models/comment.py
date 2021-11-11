from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.db.models.deletion import CASCADE, PROTECT
from django.conf import settings
from models.monster import Monster

class Comment(models.Model):
    user = ForeignKey(User,on_delete=models.PROTECT, null=True)
    monster = ForeignKey(Monster,on_delete=models.PROTECT, null=True)
    content = models.CharField(max_length=10000, null=True)

    def __str__(self) -> str:
        return self.content