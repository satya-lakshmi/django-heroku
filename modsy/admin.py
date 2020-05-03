
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import room
from .models import goal
from .models import design
from .models import furniture
from .models import project
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


from django.utils.safestring import mark_safe

UserModel = get_user_model()

admin.site.unregister(UserModel)

@admin.register(UserModel)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'user_project'
    )

    def user_project(self, obj):
        url = '/admin/modsy/project/{}/change/'.format(obj.project.pk)
        return mark_safe('<a href="{}">view project</a>'.format(url))
        list_diplay = ('Room','Goal','Design','Furniture')



# Register your models here.

admin.site.register(room)
admin.site.register(goal)
admin.site.register(design)
admin.site.register(furniture)




class ProjectAdmin(admin.ModelAdmin):
	readonly_fields = ('user','room','goal','design','furniture','created_at','updated_at')

admin.site.register(project,ProjectAdmin)

