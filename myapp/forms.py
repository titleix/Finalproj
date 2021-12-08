from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Todo, Profile, Comment, Forum


class userProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    # age = forms.IntegerField(required=True)
    # bio = forms.CharField(max_length=150, help_text='150 characters max.')
    # image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']



class CreateForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = "__all__"


class todoform(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
