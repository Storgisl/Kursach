from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_page.urls'), name='profile'),
    path('', include('articles.urls'), name='articles'),
    path('', include('courses.urls'), name='courses'),
    path('', include('profiles.urls'), name='profile'),
    path('', include('videos.urls'), name='videos'),
    path('', include('reg_page.urls'), name='registration'),
    path('', include('log_page.urls'), name='login'),
        path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)