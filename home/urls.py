
from django.urls import path,include
from .views import *
app_name="home"
urlpatterns = [

    path('', home, name='home'),
    path('about', about, name='about'),
    path('portfolio', portfolio, name='portfolio'),
    path('price', price,name='price'),
    path('services', services, name='services'),
    path('blog-home',blog_home,name='blog-home'),
    path('blog-single',blog_single,name='blog-single'),
    path('contact',contact,name='contact'),
    path('elements',elements,name='elements')


]
