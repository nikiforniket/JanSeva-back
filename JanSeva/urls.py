"""
URL configuration for JanSeva project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from juser.urls import juser_urls
from civic.urls import civic_urlpatterns
from legislator.urls import legislator_urlpatterns
from location.urls import location_urlpatterns
from news.urls import news_urlpatterns

urlpatterns = (
    [
        path("admin/", admin.site.urls),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + juser_urls
    + civic_urlpatterns
    + legislator_urlpatterns
    + location_urlpatterns
    + news_urlpatterns
)
