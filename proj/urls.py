"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from hello.views import  addreceipe, delete_receipe,  login_page, logout_page,receipes, register, update_receipe,category_recipes,landing

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from proj import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('receipes/', receipes, name='receipes'),
    path('delete_receipe/<int:id>/', delete_receipe, name='delete_receipe'),
    path('update_receipe/<int:id>/', update_receipe, name='update_receipe'),
    path('register/', register, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('addreceipe/', addreceipe, name='addreceipe'),
    path('categories/<str:category>/', category_recipes, name='category_recipes'),
    path('', landing, name='landing'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns +=staticfiles_urlpatterns()