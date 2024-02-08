from django.shortcuts import render
from .models import Course,Learning,Subject,Video,UserCourse,Contact
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.
@login_required
def educational_content(request):
    courses=Course.objects.filter(active='True')    
    return render(request,template_name="Resources/educational.html",context={"courses":courses})


def CourseOverview(request,slug):
    # print(slug)
    course=Course.objects.get(slug=slug)
    learnings=Learning.objects.filter(course=course)
    subject=Subject.objects.filter(course=course)
    video=Video.objects.filter(course=course)
    course_id=Course.objects.get(slug=slug)
    try:
        check_enroll=UserCourse.objects.filter(user=request.user,course=course_id)
        print(check_enroll)
    except UserCourse.DoesNotExist:
        check_enroll=None
        print(check_enroll)
    # video=Video.objects.filter(subject=subject).first()
    # print(video)
    if check_enroll and len(check_enroll) > 0:
        # User is enrolled in the course.
        button_text = "Already Enrolled"
    else:
        # User is not enrolled in the course.
        button_text = "Enroll"


    

    context={
        "course":course,
        "video":video,
        "learnings":learnings,
        "subjects":subject,
        'check_enroll':check_enroll,
        "button_text":button_text,
        # "video":video,
    }

    return render(request,template_name="Resources/course_overview.html",context=context)



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
