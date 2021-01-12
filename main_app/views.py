from django.shortcuts import render, redirect   # import redirect
# render is used to render the templates.
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import AuthenticationForm  # for adding the usercreation and authentication form in the webpage.
from django.contrib.auth import login,logout,authenticate   # for login , logout and authentication of the form
from django.contrib import messages
from .forms import NewUserForm  # our own modified form instead of UserCreationForm 

def homepage(request):
    #   template_name tells where to find that file in the project, context what to pass as a template here tutorials.
    return render(request = request,template_name = 'main_app/home.html',context={'tutorials' : Tutorial.objects.all})


# here the method register has argument that is get request while the form creates the post request.
def register(request):
    # as form creates the POST request.
    if request.method == 'POST':
        form = NewUserForm(data = request.POST)
        if form.is_valid():
            user = form.save()  # user created.
            username = form.cleaned_data.get('username')
            messages.success(request,f"New Account Created : {username}")
            login(request,user)
            messages.info(request,f"You are logged in as  {username}")
            return redirect("main_app:homepage")    # to redirect to the homepage function from the urls.py .
        else:
            for msg in form.error_messages:     #error_messages is dictonary
                messages.error(request,f"{msg} : {form.error_messages[msg]}")

    form = NewUserForm
    return render(request = request,template_name = 'main_app/register.html',context={"form":form})


def logout_request(request):
    logout(request)
    messages.info(request,'Logout Succesfully!!')
    return redirect("main_app:homepage")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=  request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username,password = password)
            if user is not None:
                login(request,user)
                messages.info(request,f'You are now logged in as {username}')
                return redirect("main_app:homepage")   # redirect to the same page.
            else:
                messages.error(request,"Invalid username or password")
        else:        
            messages.error(request,"Invalid username or password")

    form = AuthenticationForm()
    return render(request = request , template_name = 'main_app/login.html',context={"form":form})
