from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Course, Question, Reply

# Register your models here.


class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Course, AdminVideo)
admin.site.register(Question)
admin.site.register(Reply)
