from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name = 'home'),
  path('blog/', views.blog, name = 'blog_page'),
  path('post/<str:pk>', views.post, name = 'post'),
]