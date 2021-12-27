from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('home', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('category_new', views.category_new, name="category_new"),
    path('register', views.register, name="register"),
    path('check_user/', views.check_user, name="check_user"),
    path('user_login/', views.user_login, name="user_login"),
    path('customer', views.customer, name="customer"),
    path('seller', views.seller, name="seller"),
    path('user_logout', views.user_logout, name="user_logout"),
    path('edit_profile' ,views.edit_profile, name="edit_profile" )
    




]+ static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)