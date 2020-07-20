from . import views
from django.urls import path
app_name = 'blogs'
urlpatterns = [
    path('', views.all_blogs, name = 'all_blogs'),
    path('<int:blog_id>/', views.some_blog, name = 'some_blog'),
]
