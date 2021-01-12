from django.urls import path 
from . import views     # relative importing in the python.  
app_name = 'main_app'
urlpatterns = [
    path('',views.homepage,name='homepage'),     # it will return the function homepage from the views.py file.
    path('register/',views.register,name = 'register'),
    path('logout/',views.logout_request,name='logout'),     # function name is logout_request. we can't name is logout because it will overwrite.
    path('login/',views.login_request, name='login'),
]