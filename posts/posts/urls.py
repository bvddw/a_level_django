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
from django.urls import path, re_path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page),
    path('about/', views.about),
    path('profile/<str:username>/', views.profile),
    path('set-password/', views.set_password),
    path('set-userdata/', views.set_userdata),
    path('deactivate/', views.deactivate),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('topics/', views.topics),
    path('topics/<topic_title>/subscribe/', views.subscribe_topic),
    path('topics/<topic_title>/unsubscribe/', views.unsubscribe_topic),
    path('create/', views.create_article),
    re_path(r'^archive\/(?P<year>\d{4})\/(?P<month>1[0-2]|0?[1-9])\/$', views.archive),
    path('<article_title>/', views.article),
    path('<article_title>/comments/', views.article_comment),
    path('<article_title>/update/', views.update_article),
    path('<article_title>/delete/', views.delete_article),
]
