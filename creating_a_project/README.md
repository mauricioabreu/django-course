# Creating a project

To create a Django project we can use a management command.
A management command is a command executed via terminal to accomplish tasks like: creating a project, running the Django test web server, running third-party commands and even custom commands designed by yourself.

Open your preferred console and type the following command:

    django-admin.py startproject news

Where startproject is the command to create a project and news is the name of the project.

For this course we are going to create a simple News portal.

After executing the command above you can see that a structure of files and folders were created. Your structure should look like this:

    news
        manage.py
        news
            settings.py
            urls.py
            wsgi.py
            __init__.py


`news` is the root folder project.
`manage.py` is a management command script responsible for things like starting a new app, executing tests, running a shell interface and more daily commands.
`settings.py` file is responsible for storing all your project settings like databases used, caching engines, internationalization, third-party settings and even your custom settings.
`urls.py` is a file containing all url patterns. Whenever you request a URL to your project it checks if the pattern existis in urls.py.
`__init__.py` is a empty file used to indicate that the folder news is actually a package.

## Creating the database

For this project sqlite will be used. SQLite is a self-contained database engine that used disk filed for write/read.

Django already sets sqlite as the default database so you don't need to deal with it right now.
A management command comes with Django to easily handle new databases setup.

    python manage.py syncdb

    Creating tables ...
    Creating table django_admin_log
    Creating table auth_permission
    Creating table auth_group_permissions
    Creating table auth_group
    Creating table auth_user_groups
    Creating table auth_user_user_permissions
    Creating table auth_user
    Creating table django_content_type
    Creating table django_session

    You just installed Django's auth system, which means you don't have any superusers defined.
    Would you like to create one now? (yes/no): yes
    Username (leave blank to use 'maugzoide'): admin
    Email address:
    Password:
    Password (again):
    Superuser created successfully.
    Installing custom SQL ...
    Installing indexes ...
    Installed 0 object(s) from 0 fixture(s)

Whenever you create a database Django offers the possibility to create a superuser. A superuser is a user that has all permissions installed so superuser has access to everything on the news project.
For the project we are going to use admin/admin.

`syncdb` creates internal Django tables like django_session used to store sessions after setting 'Keep logged in' on a website.

## Test server

Django comes with an internal test server. This server is mostly used to test your project. Don't use it on a production environment. To start the server:

    python manage.py runserver

Enter the address `http://localhost:8000/` in your browser. You should see a message like 'It worked!'.
