from django.contrib import admin
from .models import User, HeroListModel, Candidate
from rest_framework.authtoken.admin import TokenAdmin


# Register your models here.
admin.site.register(User)
admin.site.register(HeroListModel)
admin.site.register(Candidate)
TokenAdmin.raw_id_fields = ['user']
