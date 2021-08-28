"""clonealba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from mainApp.views import *

#for url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('detail/<int:id>/', detail, name='detail'),
    path('register', register, name='register'),
    path('register/', registerPage, name='registerPage'),
    path('delete/<int:id>/', delete, name='delete'),
    path('update_page/<int:id>/', update_page, name="update_page"),
    path('update/<int:id>/', update, name='update'),
    path('apply/<int:id>/', apply, name='apply'),
    path('cancel/<int:id>/', cancel, name='cancel'),
    path('detail/<int:id>/comments/new/', newComment, name='newComment'),
    path('detail/<int:id>/comments/delete/<int:comment_id>', deleteComment, name='deleteComment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
