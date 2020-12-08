from django.contrib import admin

# Register your models here.
from .models import Hero
admin.site.register(Hero)

from .models import Diamond
admin.site.register(Diamond)