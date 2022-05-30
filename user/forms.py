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
    username = forms.CharField(max_length=100,
                               required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    profil_pic = forms.ImageField(widget=forms.FileInput())
    profil_bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

    class Meta:
        model = Profile
        fields = ['profil_pic', 'profil_bio']