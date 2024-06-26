from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.forms import ModelForm
from accounts.models import MyUser

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

user = get_user_model()


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=255, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-SignupForm'
        self.helper.form_method = 'post'
        self.helper.attrs = {'novalidate': ''}
        self.helper.add_input(Submit('submit', 'Submit')),
        self.helper.add_input(Submit('cancel', 'Cancel', css_class='btn-danger'))


    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Passwords do not match")
        email_qs = MyUser.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-LoginForm'
        self.helper.form_method = 'post'
        self.helper.attrs = {'novalidate': ''}
        self.helper.add_input(Submit('submit', 'Submit')),
        self.helper.add_input(Submit('cancel', 'Cancel', css_class='btn-danger'))

    def clean(self, *args, **kwargs):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Invalid username or password")
            if not password:
                raise forms.ValidationError("Invalid password")
        return super(LoginForm, self).clean(*args, **kwargs)
