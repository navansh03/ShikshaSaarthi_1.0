from django.contrib import admin
from .models import Course,Prerequisites,Learning,Video,Subject,UserCourse,Contact



# Register your models here.



class LearningAdmin(admin.TabularInline):
    model=Learning
class PrerequisitesAdmin(admin.TabularInline):
    model=Prerequisites

class SubjectAdmin(admin.TabularInline):
    model=Subject
class VideoAdmin(admin.StackedInline):
    model=Video
class CourseAdmin(admin.ModelAdmin):
    inlines =[ LearningAdmin, PrerequisitesAdmin,SubjectAdmin, VideoAdmin]





admin.site.register(Course,CourseAdmin)
admin.site.register(Subject)

admin.site.register(Video)
admin.site.register(UserCourse)

admin.site.register(Contact)