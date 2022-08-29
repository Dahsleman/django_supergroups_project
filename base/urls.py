from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('', views.home, name="home"),
    path('bot/', views.apps, name="bot"),
    path('token/', views.token, name="token"),

    path('group-settings/<str:pk>/', views.groupSettings, name="group-settings"),
    path('create-group/', views.createGroup, name="create-group"),
    path('update-group/<str:pk>/', views.updateGroup, name="update-group"),
    path('delete-group/<str:pk>/', views.deleteGroup, name="delete-group"),
    path('group-guest-list/<str:pk>/', views.groupGuest_list, name="group-guest-list"),

    path('event_type_availabilities/<str:pk>/', views.event_type_availabilities, name="event_type_availabilities"),
    path('create-event_type/<str:pk>/', views.createEvent_type, name="create-event_type"),
    path('update-event_type/<str:pk>/', views.updateEvent_type, name="update-event_type"),
    path('delete-event_type/<str:pk>/', views.deleteEvent_type, name="delete-event_type"),

    path('create-participants/<str:pk>/', views.createParticipants, name="create-participants"),

    path('events/', views.Events, name="events"),

]