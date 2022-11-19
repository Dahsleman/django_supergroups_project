from django.urls import path
from . import views


urlpatterns = [

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('', views.home, name="home"),
    path('group-settings/<str:pk>/', views.groupSettings, name="group-settings"),
    path('create-group/', views.createGroup, name="create-group"),
    path('update-group/<str:pk>/', views.updateGroup, name="update-group"),
    path('delete-group/<str:pk>/', views.deleteGroup, name="delete-group"),
    path('group-members/<str:pk>/', views.groupMembers, name="group-members"),

    path('account-user-profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('account-auth/', views.auth, name="telegram"),
    path('account-auth-token/', views.token, name="token"),

    path('settings-OH/', views.settingsOH, name="telegram-settings-OH"),
    path('settings-OH-update/', views.settingsOH_update, name="telegram-settings-OH-update"),
    path('settings-VM/', views.settingsVM, name="telegram-settings-VM"),
    path('settings-VM-update/', views.settingsVM_update, name="telegram-settings-VM-update"),
    path('settings-TZ/', views.settingsTZ, name="telegram-settings-TZ"),
    path('settings-TZ-update/', views.settingsTZ_update, name="telegram-settings-TZ-update"),

    path('agenda-create/', views.agendaCreate, name="agenda-create"),
    path('agenda-detail/<int:id>/', views.agendaDetail, name="agenda-detail"),
    path('hx/agenda-detail/<int:id>/', views.agendaDetail_HX, name="hx-agenda-detail"),
    path('agenda-update/<int:id>/', views.agendaUpdate, name="agenda-update"),
    path('agenda-delete/<int:id>/', views.agendaDelete, name="agenda-delete"),
    
    path('hx/agenda-create/<int:parent_id>/monday/', views.mondayCreateUpdate_HX, name="hx-monday-create"),
    path('hx/agenda-update/<int:parent_id>/monday/<int:id>/', views.mondayCreateUpdate_HX, name="hx-monday-update"),
    path('monday-delete/<int:parent_id>/monday/<int:id>/', views.mondayDelete, name="monday-delete"),

]