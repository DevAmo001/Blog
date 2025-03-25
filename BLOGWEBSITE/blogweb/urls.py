from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name = 'home'),
  path('blog/', views.blog, name = 'blog_page'),
  path('about/', views.about, name = 'about_page'),
  path('contact/', views.contact, name = 'contact_page'),
  path('learnmore/', views.learn_more, name = 'learnmore_page'),
  path('post/<str:pk>', views.post, name = 'post'),
]