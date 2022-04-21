"""TODOApp URL Configuration

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
from home.views import home,tododetails,CreateTodo, update,todo_delete, fulltime,internship,remote,freelance,parttime,midlevel,senior,junior,form

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('fulltime/',fulltime, name="fulltime"),
    path('senior/',senior, name="senior"),
    path('junior/',junior, name="junior"),
    path('form/',form, name="form"),
    path('midlevel/',midlevel, name="midlevel"),
    path('internship/',internship, name="internship"),
    path('freelance/',freelance, name="freelance"),
    path('parttime/', parttime, name="parttime"),
    path('remote/',remote, name="remote"),
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('create/', CreateTodo, name="create"),
    path('<id>/update/', update, name="update"),
   path('<id>/delete/', todo_delete, name="todo_delete"),
    path('<str:pk>/', tododetails, name="tododetails"),
  
    

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)