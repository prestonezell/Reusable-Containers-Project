"""mysite URL Configuration

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
from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('update_product_status/<int:product_id>/', views.update_product_status, name='update_product_status'),
    path('', views.homepage, name='homepage'),
    path('homepage.html', views.homepage, name='homepage'),
    path('registration.html', views.registration, name='registration'),
    path('login.html', views.login, name='login'),
    path('user_dashboard.html', views.user_dashboard, name='user_dashboard'),
    path('about.html', views.about, name='about'),
    path('logout.html', views.user_logout, name='user_logout'),
    path('view_products.html', views.view_products, name='view_products'),
    path('buy/<int:product_id>/', views.buy_product, name='buy_product'),
    path('give-to-collector/<int:product_id>/', views.give_to_collector, name='give_to_collector'),
    path('track_products.html', views.track_products_with_collector, name='track_products_with_collector'),
    path('return-to-available/<int:product_id>/', views.return_product_to_available, name='return_product_to_available'),
]
