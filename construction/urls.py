from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('constructions/', views.constructions, name='constructions'),
    path('constructions/new/', views.new_construction, name='new'),
    path('constructions/edit/<int:id>/', views.edit_construction, name='edit'),
    path('constructions/delete/<int:id>/', views.delete, name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
