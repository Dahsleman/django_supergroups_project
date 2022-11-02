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
    path('telegram-settings-VM-update/', views.telegramSettingsVM_update, name="telegram-settings-VM-update"),

    path('telegram-settings-TZ/', views.telegramSettingsTZ, name="telegram-settings-TZ"),
    path('telegram-settings-TZ-update/', views.telegramSettingsTZ_update, name="telegram-settings-TZ-update"),
    
    path('telegram-agenda-list/', views.telegramAgenda_list, name="telegram-agenda-list"),
    path('telegram-agenda-create/', views.telegramAgenda_create, name="telegram-agenda-create"),
    path('telegram-agenda-update/<int:id>/', views.telegramAgenda_update, name="telegram-agenda-update"),
    path('telegram-agenda-delete/<int:id>/', views.telegramAgenda_delete, name="telegram-agenda-delete"),
    path('telegram-agenda-detail/<int:id>/', views.telegramAgenda_detail, name="telegram-agenda-detail"),

    path('hx/telegram-agenda-detail/<int:id>/', views.telegramAgenda_detail_hx, name="hx-telegram-agenda-detail"),

    path('monday-delete/<int:parent_id>/monday/<int:id>/', views.telegramMonday_delete, name="monday-delete"),
    
    path('hx/telegram-agenda-detail/<int:parent_id>/monday/<int:id>/', views.telegramMonday_update_hx, name="hx-monday-detail"),
    path('hx/telegram-agenda-create/<int:parent_id>/monday/', views.telegramMonday_update_hx, name="hx-monday-create"),

    path('group-settings/<str:pk>/', views.groupSettings, name="group-settings"),
    path('create-group/', views.createGroup, name="create-group"),
    path('update-group/<str:pk>/', views.updateGroup, name="update-group"),
    path('delete-group/<str:pk>/', views.deleteGroup, name="delete-group"),
    path('group-members/<str:pk>/', views.groupMembers, name="group-members"),

    path('user-profile/<str:pk>/', views.userProfile, name="user-profile"),

    # path('create-participants/<str:pk>/', views.createParticipants, name="create-participants"),

    path('test/', views.testUpdate, name="test"),


]