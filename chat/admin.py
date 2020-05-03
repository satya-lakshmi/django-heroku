from django.contrib import admin
from chat.models import Message, UserProfile

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


from django.utils.safestring import mark_safe






# Register your models here.








# Register your models here.
admin.site.register(Message)
admin.site.register(UserProfile)
