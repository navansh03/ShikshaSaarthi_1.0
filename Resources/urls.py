from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from . import views as resources_views


urlpatterns = [
    path('educational_content/',resources_views.educational_content,name='educational_content'),
    path('course/<str:slug>/',resources_views.CourseOverview,name='coursepage'),
    path('subject/<str:slug>',resources_views.SubjectOverview,name='subjectpage'),

    path('job-listings/',resources_views.job_listings,name='job_listings'),

    path('mentor/',resources_views.mentor,name='mentor'),
    path('news/',resources_views.news,name='news'),
    path('gov_documentation/',resources_views.gov_documentations,name='gov_documentation'),
    path('course/checkout/<slug:slug>',resources_views.Checkout,name='checkout'),
         


]



if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)