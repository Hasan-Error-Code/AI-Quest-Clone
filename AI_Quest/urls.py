"""
URL configuration for AI_Quest project.

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bd/', include('Big_Data.urls')),
    path('blogs/', include('Blogs.urls')),
    path('contact/', include('Contact.urls')),
    path('da/', include('DA.urls')),
    path('dplai/', include('DeepL_and_AI.urls')),
    path('django/', include('Django.urls')),
    path('lcourse/', include('LIVE_Courses.urls')),
    path('python/', include('Python.urls')),
]
