from django.contrib import admin
from .models import TeacherRegister, Profile, Help, ContactUs
from . import models
from .models import User


admin.site.register(TeacherRegister)
admin.site.register(Profile)
admin.site.register(Help)
admin.site.register(ContactUs)


class SubAdminArea(admin.AdminSite):
    site_header = 'Sub Database'


class TRegistrationPermission(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class UserExcessPermission(admin.ModelAdmin):
    search_fields = ('email',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return obj is None or obj.username != 'admin' and obj.username != 'subadmin'

    def has_view_permission(self, request, obj=None):
        return obj is None or obj.username != 'admin'

    def has_delete_permission(self, request, obj=None):
        return False


class HelpPermission(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


class ProductPermission(admin.ModelAdmin):
    search_fields = ('product_name', 'category', 'price',)

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


subadmin_site = SubAdminArea(name='SubAdminArea')
subadmin_site.register(models.TeacherRegister, TRegistrationPermission)
subadmin_site.register(models.User, UserExcessPermission)
subadmin_site.register(models.Help, HelpPermission)



