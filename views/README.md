# Views

A view is a python function that receives a request from a client and returns a response.
A request can be made through a command line tool or a web browser.
A response can be plain text, HTML, XML, images, musics or videos. All the function should do is to return an HTTP response.

Let's create our first view:

`news/link/views.py`

```python
from django.http import HttpResponse

def hello_world(request):
    message = 'Hey, this is my first view!'
    return HttpResponse(message)
```

To test this view we need to create an entry for it in the urls.py

Let's add our app to the url router:

`news/news/urls.py`

```python
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'link/', include('link.urls')),
)
```

Now everything that hits `localhost:8000/link` will read entries from `news/link/urls.py`.
