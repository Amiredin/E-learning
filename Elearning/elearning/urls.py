from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from  . import views


urlpatterns = [
    
    path('', views.home, name='elearning-home'),
    path('about/', views.about, name='elearning-about'),
    path('five/', views.five, name='elearning-five'),
    path('six/', views.six, name='elearning-six'),
    path('seven/', views.seven, name='elearning-seven'),
    path('eight/', views.eight, name='elearning-eight'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)