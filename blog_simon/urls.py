"""
URL configuration for blog_simon project.

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
from django.urls import path
from publication_article.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('publier_article', template_publier_article, name='publier_article'),
    path('afficher_article', template_afficher_article, name='afficher_article'),
    path('creer_compte', template_creer_compte, name='creer_compte'),
    path('', template_se_connecter, name='se_connecter'),
    path('se_deconnecter', se_deconnecter, name='se_deconnecter'),
    path('commenter', commenter, name='commenter'),
]
