from cProfile import label
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Profile

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {'username':'User Name', 'email':'Email', 'password1' : 'Password', 'password2':'Repeat Password'}
        
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['username'].widget.attrs.update({'placeholder':'🤗 Enter user name', 'class':'form-input', 'style':' padding: .5rem 1rem;  border-color: #0D6EFD; margin: .5rem 0;'})
        self.fields['email'].widget.attrs.update({'placeholder':'📬 Enter email address', 'class':'form-input', 'style':' padding: .5rem 1rem;  border-color: #0D6EFD; margin: .5rem 0;'})
        self.fields['password1'].widget.attrs.update({'placeholder':'🗝 Enter password', 'class':'form-input', 'style':' padding: .5rem 1rem;  border-color: #0D6EFD; margin: .5rem 0;'})        
        self.fields['password2'].widget.attrs.update({'placeholder':'🗝 Retype password', 'class':'form-input', 'style':' padding: .5rem 1rem;  border-color: #0D6EFD; margin: .5rem 0;'})

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': '🤗 Enter your user name', 'style':'margin:1rem 0;'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'🗝 Enter your password','style':'margin:1rem 0;'}))


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'style':'margin-top: .5rem; padding: .5rem 1rem;  border-color: #0D6EFD;' }),
            'email': forms.EmailInput(attrs={ 'style':'margin-top: .5rem; padding: .5rem 1rem;  border-color: #0D6EFD;' }),
        }


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
        labels = {'profile_pic': 'Profile Picture:', 'profile_bio': 'Profile Biography: '}
        widgets = {
            'profile_bio': forms.Textarea(attrs={'placeholder': '💪 What are you going to do?', 'class': 'input-style', 'rows' :5,'col':500, 'style':'resize:none; margin-top: .5rem; padding: .5rem ;  border-color: #0D6EFD;' }),

            'profile_pic': forms.ClearableFileInput(attrs={ 'style':'margin-top: .5rem; padding: .5rem 1rem;  border-color: #0D6EFD;' }),
        }