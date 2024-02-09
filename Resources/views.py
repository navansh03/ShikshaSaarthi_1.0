from django.shortcuts import render
from .models import Course,Subject,Video,UserCourse,Contact
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import get_object_or_404


# Create your views here.
@login_required
def educational_content(request,slug):
    courses=Course.objects.filter(active='True') 
       
    return render(request,template_name="Resources/educational.html",context={"courses":courses})


def CourseOverview(request,slug):
    print(slug)
    course=Course.objects.get(slug=slug)
    subject=Subject.objects.filter(course=course)
    

    context={
        "course":course,
        "subjects":subject,
        # "video":video,
    }

    return render(request,template_name="Resources/course_overview2.html",context=context)



# def SubjectOverview(request,slug):
#     print(slug)
#     subject=Subject.objects.filter(slug2=slug)
#     video=Video.objects.filter(subject=subject)
    

#     context={
#         "subjects":subject,
#         "object":video,
#     }

#     return render(request,template_name="Resources/subject_overview.html",context=context)

def SubjectOverview(request, slug):
    subject = get_object_or_404(Subject, slug2=slug)
    videos = Video.objects.filter(subject=subject)

    context = {
        "subject": subject,
        "videos": videos,
    }

    return render(request, template_name="Resources/subject_overview.html", context=context)
# def Overview(request,slug):
#     print(slug)
#     subject=Subject.objects.filter(slug2=slug)
    

#     context={
#         "subjects":subject,
#         # "video":video,
#     }

#     return render(request,template_name="Resources/subject_overview.html",context=context)




def job_listings(request):
    return render(request,template_name='Resources/job_listings.html')


def gov_documentations(request):
    return render(request,template_name='Resources/gov_documentation.html')

def mentor(request):
    return render(request,template_name='Resources/mentor2.html')

def news(request):
    return render(request,template_name='Resources/news.html')



def Checkout(request,slug):
        course=Course.objects.get(slug=slug)
        course=UserCourse(user=request.user,course=course)
        course.save()
        checkout_url = reverse('checkout', args=['your-slug-value'])
        print(checkout_url)
        

        return render(request,'Resources/checkout_confirmation.html',{'checkout_url': checkout_url})    


# def contact_us(request):

def index(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()

        

    return render(request,'Resources/contact_us.html')



def index2(request):
    return render(request,'Resources/contact_success.html')
