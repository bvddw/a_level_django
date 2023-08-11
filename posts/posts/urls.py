"""
URL configuration for posts project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name='main_page'),
    path('about/', views.about, name='about_page'),
    path('profile/<username>/', views.profile, name='profile_page'),
    path('set-password/<username>/', views.set_password, name='set_password'),
    path('set-userdata/<username>/', views.set_userdata, name='set_data'),
    path('deactivate/', views.deactivate, name='deactivate'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('topics/<topic_title>/', views.one_topic, name='one_topic'),
    path('topics/<topic_title>/subscribe/', views.subscribe_topic, name='sub_topic'),
    path('topics/<topic_title>/unsubscribe/', views.unsubscribe_topic, name='unsub_topic'),
    re_path(r'^archive\/(?P<year>\d{4})\/(?P<month>1[0-2]|0?[1-9])\/$', views.archive),
    path('', include('postsapp.urls')),
]
