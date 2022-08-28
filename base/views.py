from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from base.scripts import save_token
from random import randint
from .models import Availabilities, Group
from .forms import GroupForm, AvailabilitiesForm, ParticipantsForm  
from django.contrib.auth.forms import UserCreationForm

"""LOGIN-LOGOUT-REGISTER"""

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home') 

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
           user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'username OR password does not exist')

    context = {'page': page} 
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/login_register.html', {'form': form})


def home(request):
    if request.user.is_authenticated: 
        current_user = request.user
        groups = Group.objects.filter(participants = current_user)

        group_participants = Group.objects.filter(participants = current_user)

        group_count = groups.count()
        context = {'groups': groups, 'group_count':group_count, 'group:participants':group_participants}
        return render(request, 'base/home.html', context)
    else:
        return redirect('register')

def apps(request):
    context = {}
    return render(request, 'base/bot.html', context)


@login_required(login_url='/login')
def token(request):
    if request.method == 'POST':
        token_id = randint(1000,9999)
        tokens = [
        {'number': token_id},
        ]
        save_token(token_id, request)
        context = {'tokens': tokens}
    return render(request, 'base/token.html', context)

"""GROUP"""    

def group(request, pk):
    group = Group.objects.get(id=pk)
    event_types = group.availabilities_set.all().order_by('-created')
    participants = group.participants.all().exclude(username=group.admin)

    context = {'group':group, 'event_types':event_types, 'participants':participants}

    return render(request, 'base/group.html', context)

def groupConfig(request, pk):
    group = Group.objects.get(id=pk)
    if request.method == 'POST':
        return render('group', pk=pk)
    context = {'group': group}
    return render(request, 'base/group_config.html', context)

@login_required(login_url='/login')
def createGroup(request):
    form = GroupForm()
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.admin = request.user
            group.save()
            group = Group.objects.get(participants__isnull=True)
            group.participants.add(request.user)
            group.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/group_form.html', context)

def updateGroup(request, pk):
    group = Group.objects.get(id=pk)
    form = GroupForm(instance=group)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form': form}
    return render(request, 'base/group_form.html',context)

def deleteGroup(request, pk):

    group = Group.objects.get(id=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('home')
    
    return render(request, 'base/delete.html',{'obj':group})



def event_type_availabilities(request, pk):
    event_type = Availabilities.objects.get(id=pk)

    context = {'event_type': event_type}
    return render(request, 'base/event_type_availabilities.html', context)

"""Event Type"""

def createEvent_type(request, pk):
    form = AvailabilitiesForm()
    group_instance = Group.objects.get(id=pk)

    if request.method == 'POST':
        form = AvailabilitiesForm(request.POST)
        if form.is_valid():
            availability_form = form.save(commit=False)
            availability_form.host = request.user
            availability_form.group = group_instance
            availability_form.save()
            return redirect('group', pk=group_instance.id)


    context = {'form':form}
    return render(request, 'base/group_form.html', context)

def updateEvent_type(request, pk):
    availability = Availabilities.objects.get(id=pk)
    form = AvailabilitiesForm(instance=availability)
    group_id = availability.group.id
    if request.method == 'POST':
        form = AvailabilitiesForm(request.POST, instance=availability)
        if form.is_valid():
            form.save()
            return redirect('group', pk=group_id)


    context = {'form': form}
    return render(request, 'base/group_form.html',context)

def deleteEvent_type(request, pk):

    availability = Availabilities.objects.get(id=pk)
    group_id = availability.group.id
    availability_name = availability.name
    
    if request.method == 'POST':
        availability.delete()
        return redirect('group', pk=group_id)
    
    return render(request, 'base/delete.html',{'obj':availability_name})

"""Participants"""

def createParticipants(request, pk):
    form = ParticipantsForm()
    group = Group.objects.get(id=pk)

    if request.method == 'POST':
        group = Group.objects.get(id=pk)
        form = ParticipantsForm(instance=group)
        if request.method == 'POST':
            form = ParticipantsForm(request.POST, instance=group)
            if form.is_valid():
                form.save()
                return redirect('group', pk=pk)

    context = {'form':form}
    return render(request, 'base/participant_form.html', context)


"""Events"""

def Events(request):
    context = {}
    return render(request, 'base/events.html', context)








