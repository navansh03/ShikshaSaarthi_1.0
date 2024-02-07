from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm
# ,UserUpdateForm,ProfileUpdateForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import CustomUser


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created, you can now log in as {username}!')

            # Send OTP to the user's phone number
            otp = form.send_otp()
            request.session['otp'] = otp
            request.session['user_id'] = user.id

            return redirect('otp_verification')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})



def otp_verification(request):
    if request.method == 'POST':
        # user_id = request.session.get('user_id')
        otp_entered = request.POST.get('otp')
        otp_recieved= request.session.get('otp')
        print(otp_recieved)
        otp_entered = int(otp_entered)
        print(type(otp_entered))
        print(type(otp_recieved))
        if  otp_entered ==otp_recieved :
            # user = CustomUser.objects.get(id=user_id)
            print('if condition')
            messages.success(request, 'OTP verification successful. You are now logged in.')
            return redirect('login')
        else:
            print('else condition')
            messages.error(request, 'Invalid OTP. Please try again.')
        
        print(otp_entered)
    return render(request, 'users/otp_verification.html')

@login_required
def landing_page(request):
    # course=Course.objects.get(slug=slug)
    user = request.user
    print(user)
    context={
        "user":user,
    }

    return render(request,'users/landing_page.html',context=context)
