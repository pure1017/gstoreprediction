"""webapp_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import view
from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'),
        name='home'),
    path('hello', view.hello),
    path('projects', view.project),#view.project_revenue
    path('index', view.index),
    path('about', view.about),
    path('services', view.models),
    path('linear_regression', view.linear_regression),
    path('random_forest', view.random_forest),
    path('lightGBM', view.lightGBM),
    path('gradient_boosting', view.gradient_boosting),
    path('nn', view.nn),
    path('cnn', view.cnn),
    path('blog', view.blog),
    path('contact', view.contact),
]