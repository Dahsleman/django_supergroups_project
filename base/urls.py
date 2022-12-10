from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #import this


urlpatterns = [

    path('account-user-profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('agenda-create/', views.agendaCreate, name="agenda-create"),
    path('agenda-detail/<int:id>/', views.agendaDetail, name="agenda-detail"),
    path('hx/agenda-detail/<int:id>/', views.agendaDetail_HX, name="hx-agenda-detail"),
    path('agenda-update/<int:id>/', views.agendaUpdate, name="agenda-update"),
    path('agenda-delete/<int:id>/', views.agendaDelete, name="agenda-delete"),
    
    path('hx/agenda-create/<int:parent_id>/monday/', views.mondayCreateUpdate_HX, name="hx-monday-create"),
    path('hx/agenda-update/<int:parent_id>/monday/<int:id>/', views.mondayCreateUpdate_HX, name="hx-monday-update"),
    path('monday-delete/<int:parent_id>/monday/<int:id>/', views.mondayDelete, name="monday-delete"),

    path('hx/agenda-create/<int:parent_id>/tuesday/', views.tuesdayCreateUpdate_HX, name="hx-tuesday-create"),
    path('hx/agenda-update/<int:parent_id>/tuesday/<int:id>/', views.tuesdayCreateUpdate_HX, name="hx-tuesday-update"),
    path('tuesday-delete/<int:parent_id>/tuesday/<int:id>/', views.tuesdayDelete, name="tuesday-delete"),

    path('hx/agenda-create/<int:parent_id>/wednesday/', views.wednesdayCreateUpdate_HX, name="hx-wednesday-create"),
    path('hx/agenda-update/<int:parent_id>/wednesday/<int:id>/', views.wednesdayCreateUpdate_HX, name="hx-wednesday-update"),
    path('wednesday-delete/<int:parent_id>/wednesday/<int:id>/', views.wednesdayDelete, name="wednesday-delete"),

    path('hx/agenda-create/<int:parent_id>/thursday/', views.thursdayCreateUpdate_HX, name="hx-thursday-create"),
    path('hx/agenda-update/<int:parent_id>/thursday/<int:id>/', views.thursdayCreateUpdate_HX, name="hx-thursday-update"),
    path('thursday-delete/<int:parent_id>/thursday/<int:id>/', views.thursdayDelete, name="thursday-delete"),

    path('hx/agenda-create/<int:parent_id>/friday/', views.fridayCreateUpdate_HX, name="hx-friday-create"),
    path('hx/agenda-update/<int:parent_id>/thursday/<int:id>/', views.fridayCreateUpdate_HX, name="hx-friday-update"),
    path('friday-delete/<int:parent_id>/thursday/<int:id>/', views.fridayDelete, name="friday-delete"),

    path('hx/agenda-create/<int:parent_id>/saturday/', views.saturdayCreateUpdate_HX, name="hx-saturday-create"),
    path('hx/agenda-update/<int:parent_id>/saturday/<int:id>/', views.saturdayCreateUpdate_HX, name="hx-saturday-update"),
    path('saturday-delete/<int:parent_id>/saturday/<int:id>/', views.saturdayDelete, name="saturday-delete"),

    path('hx/agenda-create/<int:parent_id>/sunday/', views.sundayCreateUpdate_HX, name="hx-sunday-create"),
    path('hx/agenda-update/<int:parent_id>/sunday/<int:id>/', views.sundayCreateUpdate_HX, name="hx-sunday-update"),
    path('sunday-delete/<int:parent_id>/sunday/<int:id>/', views.sundayDelete, name="sunday-delete"),

    path('', views.home, name="home"),







    path('group-settings/<str:pk>/', views.groupSettings, name="group-settings"),
    path('create-group/', views.createGroup, name="create-group"),
    path('update-group/<str:pk>/', views.updateGroup, name="update-group"),
    path('delete-group/<str:pk>/', views.deleteGroup, name="delete-group"),
    path('group-members/<str:pk>/', views.groupMembers, name="group-members"),
    path('settings-OH/', views.settingsOH, name="telegram-settings-OH"),
    path('settings-OH-update/', views.settingsOH_update, name="telegram-settings-OH-update"),
    path('settings-VM/', views.settingsVM, name="telegram-settings-VM"),
    path('settings-VM-update/', views.settingsVM_update, name="telegram-settings-VM-update"),
    path('settings-TZ/', views.settingsTZ, name="telegram-settings-TZ"),
    path('settings-TZ-update/', views.settingsTZ_update, name="telegram-settings-TZ-update"),
    path('account-auth/', views.auth, name="telegram"),
    path('account-auth-token/', views.token, name="token"),

]