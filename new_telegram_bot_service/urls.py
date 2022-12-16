"""new_telegram_bot_service URL Configuration

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
from django.urls import path, include, reverse
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    
    # path('register/', views.registerPage, name="register"),

    # path('password-change/',
    #     auth_views.PasswordChangeView.as_view(
    #         template_name='new_telegram_bot_service/password-change.html',
    #         success_url = '/'
    #     ),name='password_change'),

    path("password-change/", views.password_change, name="password-change"),

    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='new_telegram_bot_service/password-reset-done.html'
        ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="new_telegram_bot_service/password-reset-confirm.html"
        ), name='password_reset_confirm'),

    path('password-reset-complet/', auth_views.PasswordResetCompleteView.as_view(
        template_name='new_telegram_bot_service/password-reset-complet.html'
        ), name='password_reset_complete'), 

    path('password-reset/', views.password_reset_request, name="password_reset"),

]
