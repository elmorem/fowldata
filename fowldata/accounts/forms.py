from django import forms
from django.forms import ModelForm
from accounts.models import MyUser


# class SignUpForm(ModelForm):
#     class Meta: 
#         model = MyUser
#         fields = "__all__"

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    password = forms.CharField(max_length=255)
    password2 = forms.CharField(max_length=255)

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

    def save(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = MyUser.objects.create_user(username, email, password)
        print(user.username, user.email)
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)