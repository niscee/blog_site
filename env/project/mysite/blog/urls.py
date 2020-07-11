"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

# urlpatterns = [
#       path('', views.index, name='home'),
#       path('about/', views.about, name='about'),
# ]

""" (class based view) naming convention for class based view 
     <app>/<model>_<viewtype>.html eg - blog/post_list.html """

urlpatterns = [

      path('about/', views.about, name='about'),
      path('search/', views.search, name='search'),
      path('old_post/', views.oldPost, name='old_post'),
      path('', PostListView.as_view(template_name='blog/home.html'), name='home'),
      path('post/<int:pk>/', PostDetailView.as_view(),name="post_detail"),
      path('post/new/', PostCreateView.as_view(), name="post_create"),
      path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post_update"),
      path('post/<int:pk>/delete', PostDeleteView.as_view(), name="post_delete"),
]


