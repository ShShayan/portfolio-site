"""portfolio URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
    path('CV/', jobs.views.CV, name='CV'),
    path('portfolio/', jobs.views.portfolio, name='portfolio'),
    path('projects/', jobs.views.projects, name='projects'),
    path('blog/', include('blog.urls')),
    path('contact/', jobs.views.contact, name='contact'),
    path('portfolio/arch-portfolio', jobs.views.arch_portfolio, name='arch_portfolio'),
    path('portfolio/energy-portfolio', jobs.views.energy_portfolio, name='energy_portfolio'),
    path('portfolio/web-portfolio', jobs.views.web_portfolio, name='web_portfolio'),
    path('portfolio/photo-portfolio', jobs.views.photo_portfolio, name='photo_portfolio'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)