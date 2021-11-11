from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.db.models.deletion import CASCADE, PROTECT
from django.conf import settings
from models.stats import Stats


class Character(models.Model):
    RACES = (
       ("Human", "Human"),
       ("Elf", "Elf"),
       ("Dark Elf", "Dark Elf"),
       ("Dwarf", "Dwarf"),
       ("Halfling", "Halfling"),
       ("Teifling", "Teifling"),
       ("Aarakocra", "Aarakocra"),
       ("Dragonborn", "Dragonborn"),
       ("Genasi", "Genasi"),
       ("Gnome", "Gnome"),
       ("Goliath", "Goliath"),
       ("Half-Elf", "Half-Elf"),
       ("Half-Orc", "Half-Orc"),
       ("Aasimar", "Aasimar")
    )
    CLASS = (
       ("Barbarian", "Barbarian"),
       ("Bard", "Bard"),
       ("Cleric", "Cleric"),
       ("Druid", "Druid"),
       ("Fighter", "Fighter"),
       ("Monk", "Monk"),
       ("Paladin", "Paladin"),
       ("Ranger", "Ranger"),
       ("Rogue", "Rogue"),
       ("Sorcerer", "Sorcerer"),
       ("Warlock", "Warlock"),
       ("Wizard", "Wizard")
    )
    name = models.CharField(max_length=200, null=True)
    descript = models.CharField(max_length=10000)
    race = models.CharField(max_length=200, null=True,choices=RACES)
    classes = models.CharField(max_length=200, null=True,choices=CLASS)
    date_created = models.DateTimeField(auto_now_add=True)
    creator = ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT, null=True, default=User)
    stats = ForeignKey(Stats, on_delete=models.PROTECT,null=True)


    def __str__(self) -> str:
           return self.name