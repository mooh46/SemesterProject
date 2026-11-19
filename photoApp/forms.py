from django import forms

from photoApp.models import User


class RegisterForm(forms.Form):
    email = forms.EmailField(label='email', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
    confirmation = forms.CharField(label='Confirm Password', max_length=100, widget=forms.PasswordInput)

    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        confirmation = self.cleaned_data.get('confirmation')
        if password != confirmation:
            raise forms.ValidationError("Passwords don't match")
        return self.cleaned_data


    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(username=email).exists():
            raise forms.ValidationError("Email already exists")
        return email



class LoginForm(forms.Form):
    email = forms.EmailField(label='email', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)

    def clean_email(self):
        return self.cleaned_data['email'].lower()