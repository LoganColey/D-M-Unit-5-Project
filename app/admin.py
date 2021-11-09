from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Stats)
admin.site.register(Character)
admin.site.register(Monster)
admin.site.register(Comment)
admin.site.register(Campaign)
admin.site.register(Notes)

