from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from twilio.rest import Client
import phonenumbers
import random
from .models import CustomUser
from django.conf import settings

class UserRegistrationForm(UserCreationForm):
    phone_regex = RegexValidator(
        regex=r'^\+91\d{10}$',
        message="Phone number must be entered in the format: '+919999999999'. Exactly 10 digits allowed after the country code."
    )

    phone = forms.CharField(validators=[phone_regex], max_length=13)

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'phone']

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        try:
            parsed_phone = phonenumbers.parse(phone, 'IN')
            if not phonenumbers.is_valid_number(parsed_phone):
                raise forms.ValidationError("Invalid phone number")
        except phonenumbers.phonenumberutil.NumberFormatException:
            raise forms.ValidationError("Invalid phone number")

        return phone

    def send_otp(self):
        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)

        otp = random.randint(999,6969)# Generate a random OTP here

        message = client.messages.create(
            body=f'Your OTP from Shiksha Saarthi is : {otp}',
            from_= settings.TWILIO_PHONE_NUMBER,
            to=self.cleaned_data['phone']
        )
        print(otp)
        return otp
