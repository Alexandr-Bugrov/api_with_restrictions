
from django.contrib import admin
from rest_framework.authtoken.admin import User

from advertisements.models import Advertisement

class AdvertisementAdmin(admin.TabularInline):
    model = Advertisement
    extra = 1


class UserAdmin(admin.ModelAdmin):
    inlines = [AdvertisementAdmin]
    pass



