1)Why Django should be used for web-development? Explain how you
can create a project in Django?pip install virtualenv

High-level abstraction: Django provides high-level abstractions of common web development patterns, making it easier for
 developers to build complex applications quickly. It handles many aspects of web development such as routing, 
templating, authentication, and database manipulation out of the box.

Batteries-included: Django comes with a vast array of built-in features, tools, and libraries, which can significantly speed up 
the development process. These include an ORM (Object-Relational Mapping) for interacting with databases, an 
authentication system, a powerful admin interface, and built-in security features.

Scalability: Django is designed to scale easily, allowing applications to handle high levels of traffic and data. Its architecture 
supports the deployment of applications across multiple servers and allows for efficient caching mechanisms.

Security: Django takes security seriously and provides built-in protection against common web security threats such as SQL
 injection, cross-site scripting (XSS), cross-site request forgery (CSRF), and clickjacking. It encourages best practices for securing web applications.

Community and ecosystem: Django has a large and active community of developers who contribute plugins, packages, and documentation. This vast ecosystem makes it easy to find solutions to common problems and extend the framework's functionality.


===========Django command==========

python -m venv myenv
cd myenv
Scripts\activate
pip install django
django-admin startproject myproject
cd myproject
django-admin startapp myapp
python manage.py migrate
python manage.py runserver

python manage.py createsuperuser


---------------------------------------------------------------------------------------------
2)How to check installed version of django? 

django-admin --version
----------------------------------------------------------------------------
3)Explain what does django-admin.py make messages command is used
for? 

Runs over the entire source tree of the current directory and pulls out all strings marked for translation. It creates (or updates) 
a message file in the conf/locale (in the django tree) or locale (for projects and applications) directory. You must run this command with one of either the --locale, --exclude, or --all options

--------------------------------------------------------------------------
4)What is Django URLs?make program to create django urls

In Django, URLs (Uniform Resource Locators) are used to map URLs to views. When a user makes a request to a specific
 URL, Django uses the URL configuration defined in the urls.py file to determine which view function should handle the request.

(myapp)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

(my project)

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
---------------------------------------------------------------------------------
5)What is a QuerySet?Write program to create a new Post object in
database

-->A QuerySet is a collection of data from a database.

-->A QuerySet is built up as a list of objects.

-->QuerySets makes it easier to get the data you actually need, by allowing you to filter and order the data at an early stage.


from blog.models import Post

new_post = Post.objects.create(
    title='New Post Title',
    content='Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    author='John Doe'
)

new_post.save()
---------------------------------------------------------------------------------
6)Mention what command line can be used to load data into Django?

Django-admin.py loaddata. 
----------------------------------------------------------------------------------
7)Explain what does django-admin.py make messages command is used
for? 

Runs over the entire source tree of the current directory and pulls out all strings marked for translation. It creates (or updates) 
a message file in the conf/locale (in the django tree) or locale (for projects and applications) directory. 
-----------------------------------------------------------------