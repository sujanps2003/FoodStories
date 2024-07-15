# myproject/urls.py
from django.contrib import admin
from django.urls import path


from hello.views import name

urlpatterns = [
    path('admin/', admin.site.urls),
]
