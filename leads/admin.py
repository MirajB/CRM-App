from django.contrib import admin
from .models import lead, User, Agent
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Register your models here.
admin.site.register(lead)
admin.site.register(User)
admin.site.register(Agent)
