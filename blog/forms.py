from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .models import Profile
from django.core.exceptions import ValidationError

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Please enter a valid email address.')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with that email already exists.")
        return email

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        
        # Check if email exists but exclude the current user
        if User.objects.filter(email=email).exclude(username=username).exists():
            raise ValidationError("A user with that email already exists.")
        return email

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'location', 'website']

class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        self.subject = kwargs.pop('subject', 'Password Reset')
        super().__init__(*args, **kwargs)
    
    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        # Override the subject with our custom one
        subject = self.subject
        return super().send_mail(subject_template_name, email_template_name,
                                context, from_email, to_email, html_email_template_name) 