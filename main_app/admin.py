from django.contrib import admin
from .models import Tutorial,TutorialCategory,TutorialSeries    # importing Tutorial through relative (.models)
from tinymce.widgets import TinyMCE     # importing the app for getting the text editor in the webpage.
from django.db import models

# Register your models here.

# class for customizing the admin page.
class TutorialAdmin(admin.ModelAdmin):
    # fields:[
    #     'tutorial_field',
    #     'tutorial_published',
    #     'tutorial_content',     
    # ]   

    fieldsets = [
        ("Title/date",{"fields":["tutorial_title","tutorial_published"]}),      # arrange the title and date in the row name title/date
        ("Content",{"fields":["tutorial_content"]}),         # arrange the content in the row name Content
        ("URL",{"fields":["tutorial_slug"]}),
        ("Series",{"fields":["tutorial_series"]})
    ]

    # text editor in the TextField.
    formfield_overrides = {
        models.TextField:{'widget':TinyMCE()}   #overriding the TextField for admin
    }

# admin.site.register(Tutorial)  registering our class Tutorial. 

admin.site.register(Tutorial,TutorialAdmin)   # argument TutorialAdmin is passed to make changes in the admin form.
admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)


# pip install django-tinymce4-lite  (installing other django app) add this app to the settings.py file.