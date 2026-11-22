from django import forms

from photoApp.models import User, Post


class RegisterForm(forms.Form):
    email = forms.EmailField(label='email', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirmation = forms.CharField(label='Confirm Password', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

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


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('picture','caption')

    def  clean_picture(self):
        picture = self.cleaned_data['picture']
        #convert into bytes since picture gives file size in bytes
        if picture.size > 5 * 1024 * 1024:
            raise forms.ValidationError("Picture must be 5MB or smaller")
        if picture.content_type not in ('image/jpeg', 'image/png' ):
            raise forms.ValidationError("Picture must be jpg or png")
        return picture


class LoginForm(forms.Form):
    email = forms.EmailField(label='email', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_email(self):
        return self.cleaned_data['email'].lower()