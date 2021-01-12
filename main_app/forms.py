# customizing the form. 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):    # inherit from the UserCreationForm.
    email = forms.EmailField(required=True)     # form won't be submitted without filling the email field.

    class Meta:
        model = User    # model is based on User
        fields = ("username","email","password1","password2")
    
    def save(self,commit=True):
        user = super(NewUserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user