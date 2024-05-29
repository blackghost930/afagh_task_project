from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('address', 'phone_number', 'email', 'password1', 'password2')
        labels = {
            'age': 'سن',
            'email': 'ایمیل:',
            'username': 'نام و نام خانوادگی:',
            'password1': 'رمز عبور:',
            'password2': 'تکرار رمز عبور:',
            'address': 'آدرس:',
            'phone_number': 'شماره همراه:',

        }
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields




