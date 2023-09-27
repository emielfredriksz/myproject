"""
URL configuration for myproject project.

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
from django.urls import path, include
from myproject import views
from rest_framework import renderers

review_list = views.ReviewViewSet.as_view({
        'get':'list',
        'post': 'create'
    })

review_detail = views.ReviewViewSet.as_view({
        'get':'retrieve'
    })

review_sentiment = views.ReviewViewSet.as_view({
        'get':'sentiment'
    },  renderer_classes=[renderers.StaticHTMLRenderer])



urlpatterns = [
    path('', views.api_root),
    path('admin/', admin.site.urls),
    path('reviews/', review_list, name='review-list'),
    path('reviews/<int:pk>/', review_detail, name='review-detail'),
    path('reviews/<int:pk>/sentiment', review_sentiment, name='review-sentiment')
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
