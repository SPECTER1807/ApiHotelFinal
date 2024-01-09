"""APIHOTEL2 URL Configuration

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
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from api.views import *
from api import views





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.as_view(),name='index'),
    path('reservas.html/', views.reservas, name='reservas'),
    path('reservas_confirmacion.html', views.reservas_confirmacion, name='reservas_confirmacion'),
    path('authentication-login.html',views.login_view, name='login_view'),
    path('authentication-register.html', views.registro_view, name='registro'),
    path('dashboard.html',Dashboard.as_view(),name='dashboard'),
    path('login.html',Login.as_view(),name='login'),
    path('register.html',Register.as_view(),name='register'),
    path('about.html',About.as_view(),name='about'),
    path('amenities.html',Amenities.as_view(),name='amenities'),
    path('bookings.html',Bookings.as_view(),name='bookings'),
    path('contact.html',Contact.as_view(),name='contact'),
    path('failed.html',Failed.as_view(),name='failed'),
    path('faqs.html',Faqs.as_view(),name='faqs'),
    path('gallery.html',Gallery.as_view(),name='gallery'),
    path('privacy-policy.html',Privacy.as_view(),name='privacy'),
    path('rooms.html',Rooms.as_view(),name='rooms'),
    path('alcove.html',Alcove.as_view(),name='alcove'),
    path('cottage.html',Cottage.as_view(),name='cottage'),
    path('business-suite.html',Business.as_view(),name='business'),
    path('deluxe.html',Deluxe.as_view(),name='deluxe'),
    path('executive.html',Executive.as_view(),name='executive'),
    path('round-house.html',RoundHouse.as_view(),name='roundhouse'),
    path('studio.html',Studio.as_view(),name='studio'),
    path('vip.html',Vip.as_view(),name='vip'),
    path('vvip.html',Vvip.as_view(),name='vvip'),
    path('success.html',Success.as_view(),name='success'),
    
    # path('checkout/<int:product_id>/', views.CheckOut, name='checkout'),
    # path('payment-successful/<int:product_id>/', views.PaymentSuccessful, name='payment-successful'),
    # path('payment-failed/<int:product_id>/', views.PaymentFailed, name='payment-failed'),
    
    #  path('reservar-habitacion/', reservar_habitacion, name='reservar_habitacion'),

    
]
