

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