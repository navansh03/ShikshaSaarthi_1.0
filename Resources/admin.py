from django.contrib import admin
from .models import Course,Video,Subject,UserCourse,Contact



# Register your models here.




class SubjectAdmin(admin.TabularInline):
    model=Subject
class VideoAdmin(admin.StackedInline):
    model=Video
class CourseAdmin(admin.ModelAdmin):
    inlines =[ SubjectAdmin, VideoAdmin]





admin.site.register(Course,CourseAdmin)
admin.site.register(Subject)

admin.site.register(Video)
admin.site.register(UserCourse)

admin.site.register(Contact)