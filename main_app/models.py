from django.db import models
from datetime import datetime
# Create your models here.
# here we create our data base tables.

# class Tutorial will create a table named Tutorial with column names tutorial_title,tutorial_content,tutorial_published.
# it will create a PrimaryKey automatically.
''' 
for getting the query of creating table write the following command in the command prompt.
--python manage.py sqlmigrate main_app 0001
here 0001 is the name of the file in the folder migrations.
'''

'''
Steps to create Tables
1. Create Tables in the models.py file.
2. python manage.py makemigrations
3. python manage.py migrate
'''

'''
For Data Entry through shell
1.  python manage.py shell                  (it will enter you to the interactive shell prompt)
2.  from main_app.models import Tutorial    (importing Tutorial from main_app.models)
3.  Tutorial.objects.all()                  (displaying the current list of content in the table.)
4.  from django.utils import timezone       (importing timezone from django.utils)(optional)
5.  new_tutorial = Tutorial(tutorial_title = 'To be', tutorial_content = '....or not to be',tutorial_published = timezone.now())
In the 5th step creating object of Tutorial Class and writing data to the table.
6.  new_tutorial.save()                     (saving the content in the data)
7.  Tutorial.objects.all()                  (displaying the content of the table.)
'''


class TutorialCategory(models.Model):
    # you can explore different type of fields in djangoDocumentation under fieldtypes
    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)

    # read the django documentation for the information about class meta.
    class Meta:
        verbose_name_plural = "Categories"

    # this function is useful in displaying the name in the admin page.
    def __str__(self):
        return self.tutorial_category


class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)
    # on_delete will protect the Tutorial Series if tutorialCategory is deleted and it is used for cascading. and here default must be 1
    # foreign key to class Category.
    Tutorial_category = models.ForeignKey(
        TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series


class Tutorial(models.Model):
    # charfield are like shorter things.
    tutorial_title = models.CharField(max_length=200)
    # textField are like a blob i.e not finite lenght.
    tutorial_content = models.TextField()
    # default date is provided.
    tutorial_published = models.DateTimeField(
        'date published', default=datetime.now())

    tutorial_series = models.ForeignKey(
        TutorialSeries, verbose_name='Series', default=1, on_delete=models.SET_DEFAULT)
    tutorial_slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.tutorial_title

# tutorial point to a series and that series point to category.
