# Applications

Before starting our example project, we should explain what is an application.
Commonly called `app` a Django application is not a Django project. A project is a collection of apps and an app is a compenent that does something by your project.

To create our first app you need to be in the same directory level as manage.py and type the following command in your preferred console:

    python manage.py startapp link

An app named `link` has been created. This app is a folder with the following structure:

    link
        admin.py
        __init__.py
        models.py
        tests.py
        views.py

`link` is the root folder app.

`admin.py` is the file used to create all the views related to the built-in Django admin interface.

`__init__.py` is a empty file used to indicate that the folder news is actually a package.

`tests.py` is a file used to write tests for this app.

`views.py` is where all your views related to this app should be.

## Installed apps

`settings.py` has a very important setting. It is a tuple structure that defines which apps are part of your project. Django already comes with some installed apps like `django.contrib.admin` being responsible for all admin actions. This setting is also important when you are using third-party apps that need to be added as an installed app.

Now you understand why `INSTALLED_APPS` is important we need to add `link` to instaled apps.
This is how it should look like:

     INSTALLED_APPS = (
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'link',)

tip: Don't forget to include a comma in the end of the tuple.
