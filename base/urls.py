from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('', views.home, name="home"),

    path('telegram/', views.telegram, name="telegram"),
    path('token/', views.token, name="token"),
    path('telegram-settings-OH/', views.telegramSettingsOH, name="telegram-settings-OH"),
    path('telegram-settings-OH-update/', views.telegramSettingsOH_update, name="telegram-settings-OH-update"),

    path('telegram-settings-VM/', views.telegramSettingsVM, name="telegram-settings-VM"),
    path('telegram-settings-TZ/', views.telegramSettingsTZ, name="telegram-settings-TZ"),
    path('telegram-agenda/', views.telegramAgenda, name="telegram-agenda"),

    path('group-settings/<str:pk>/', views.groupSettings, name="group-settings"),
    path('create-group/', views.createGroup, name="create-group"),
    path('update-group/<str:pk>/', views.updateGroup, name="update-group"),
    path('delete-group/<str:pk>/', views.deleteGroup, name="delete-group"),
    path('group-members/<str:pk>/', views.groupMembers, name="group-members"),

    path('user-profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('create-participants/<str:pk>/', views.createParticipants, name="create-participants"),


]