from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from base.scripts import save_token
from random import randint
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import modelformset_factory

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

def telegram(request):
    """telegram-agenda-list"""
    agenda_objects = Agenda.objects.filter(user=request.user)
    total_objects = agenda_objects.count()+1
    num = range(1,total_objects)

    context = {
        'agenda_objects':agenda_objects,
        'num':num,
    }
    return render(request, 'base/telegram.html', context)



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

def telegramSettingsOH(request):
    current_user = request.user
    objects = Settings.objects.filter(user=current_user)
    OH_objects = Settings.objects.get(user=current_user)
    status = OH_objects.status
    time = OH_objects.time
    permanently_closed = 'permanently closed'
    set_open_and_close_time = 'set open and close time'

    context = {'objects':objects, 'status':status, 'permanently_closed':permanently_closed, 'set_open_and_close_time':set_open_and_close_time, 'time':time}
    return render(request, 'base/telegram-settings-OH.html', context)

def telegramSettingsOH_update(request):
    current_user = request.user
    opening_hours_objects = Settings.objects.get(user=current_user)
    form = Opening_hours_Form(instance=opening_hours_objects)
    if request.method == 'POST':
        form = Opening_hours_Form(request.POST, instance=opening_hours_objects)
        if form.is_valid():
            form.save()
            opening_hours_objects = Settings.objects.get(user=current_user)
            status = opening_hours_objects.status
            time = opening_hours_objects.time
            if status == 'permanently closed':
                Opening = form.save(commit=False)
                Opening.time = ""
                Opening.open_time = ""
                Opening.close_time = ""
                Opening.days = ""
                Opening.notification = ""
                form.save()
                return redirect('telegram-settings-OH')
            elif status == 'open' and time == '24 hours':
                Opening = form.save(commit=False)
                Opening.open_time = ""
                Opening.close_time = ""
                form.save()
                return redirect('telegram-settings-OH')
            else:   
                return redirect('telegram-settings-OH')

    context = {'form':form}

    return render(request, 'base/telegram-settings-OH-update.html', context)

def telegramSettingsVM(request):
    current_user = request.user
    objects = Settings.objects.filter(user=current_user)
    OH_objects = Settings.objects.get(user=current_user)
    voice_messages = OH_objects.voice_messages
    activated = 'activated'
    context = {'objects':objects, 'voice_messages':voice_messages, 'activated':activated}
    return render(request, 'base/telegram-settings-VM.html', context)

def telegramSettingsVM_update(request):
    current_user = request.user
    opening_hours_objects = Settings.objects.get(user=current_user)
    form = Voice_messagesForm(instance=opening_hours_objects)
    if request.method == 'POST':
        form = Voice_messagesForm(request.POST, instance=opening_hours_objects)
        if form.is_valid():
            form.save()
            objects = Settings.objects.get(user=current_user)
            voice_messages = objects.voice_messages
            if voice_messages == 'inactivated':
                objects = form.save(commit=False)
                objects.voice_messages_notification = ""
                form.save()
                return redirect('telegram-settings-VM')
            else:
                return redirect('telegram-settings-VM')
    
    context = {'form':form}
    return render(request, 'base/telegram-settings-VM-update.html', context)

def telegramSettingsTZ(request):
    current_user = request.user
    objects = Settings.objects.filter(user=current_user)
    context = {'objects':objects}
    return render(request, 'base/telegram-settings-TZ.html', context)

def telegramSettingsTZ_update(request):
    current_user = request.user
    opening_hours_objects = Settings.objects.get(user=current_user)
    form = TimezoneForm(instance=opening_hours_objects)
    if request.method == 'POST':
        form = TimezoneForm(request.POST, instance=opening_hours_objects)
        if form.is_valid():
            form.save()
            return redirect('telegram-settings-TZ')

    context = {'form':form}
    return render(request, 'base/telegram-settings-TZ-update.html', context)


"""Agenda"""


@login_required
def telegramAgenda_list(request):
    agenda_objects = Agenda.objects.filter(user=request.user)
    settings_objs = Settings.objects.filter(user=request.user)

    context = {
        'agenda_objects':agenda_objects,
        'settings_objs':settings_objs,
    }

    return render(request, 'base/telegram-agenda-list.html', context)


@login_required
def telegramAgenda_detail(request, id=None):
    agenda_obj = get_object_or_404(Agenda, id=id, user=request.user)
    context = {
        'agenda_obj':agenda_obj,
    }
    return render(request, 'base/telegram-agenda-detail.html', context)

@login_required
def telegramAgenda_hx(request, id):
    user = request.user
    settings_objs = Settings.objects.filter(user=user)
    agenda_objs = Agenda.objects.get(user=user, id=id)
    objs_children = MondaySquedules.objects.filter(agenda__user=user)
    context = {
        'settings_objs':settings_objs,
        'agenda_objs':agenda_objs,
        'objs_children':objs_children,
    }
    return render(request, 'base/partials/telegram-agenda.html', context)

@login_required
def telegramAgenda_create(request):
    form = AgendaForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('telegram-agenda-list')
    return render(request, 'base/telegram-agenda-create-update.html', context)

@login_required
def telegramAgenda_update(request, id=None):
    agenda_obj = get_object_or_404(Agenda, id=id, user=request.user)
    form = AgendaForm(request.POST or None, instance=agenda_obj)
    MondayScheduleFormset=modelformset_factory(MondaySquedules, form=MondayScheduleForm, extra=0)
    qs = agenda_obj.mondaysquedules_set.all()
    formset=MondayScheduleFormset(request.POST or None, queryset=qs)
    context = {
        'form':form,
        'formset':formset,
        'agenda_obj':agenda_obj,
        }
    
    if all([form.is_valid(),formset.is_valid()]):
        parent=form.save(commit=False)
        parent.save()
        for form in formset:
            child=form.save(commit=False)
            if child.agenda is None:
                child.agenda = parent
            child.save()
        context['message'] = 'Data saved'

    return render(request, 'base/telegram-agenda-create-update.html', context)

"""GROUP"""    

def groupSettings(request, pk):
    group = Group.objects.get(id=pk)
    participants = group.participants.all().exclude(username=group.admin)

    context = {'group':group, 'participants':participants}

    return render(request, 'base/group_settings.html', context)

def groupMembers(request, pk):
    group = Group.objects.get(id=pk)
    participants = group.participants.all().exclude(username=group.admin)
    group_type = 'Private'
    private_type = Group_type.objects.get(id='2')

    
    if request.method == 'POST':
        return render('group-settings', pk=pk)

    context = {'group': group, 'participants':participants, 'group_type':group_type, 'private_type':private_type}
    return render(request, 'base/group_members.html', context)

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
    
    return render(request, 'base/group_delete.html',{'obj':group})

def userProfile(request, pk):
    users = User.objects.get(id=pk)

    context = {'users':users}
    return render(request, 'base/user_profile.html', context)

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

"""Form Test"""

# def test(request):
#     form = Opening_hours_Form()
#     if request.method == 'POST':
#         form = Opening_hours_Form(request.POST)
#         if form.is_valid():
#             Opening = form.save(commit=False)
#             Opening.user = request.user
#             form.save()
#             return redirect('home')

#     context = {'form':form}

#     return render(request, 'base/test.html', context)

def testUpdate(request):
    user = request.user

    obj = Agenda.objects.get(user=user)
    form = AgendaForm(instance=obj)
    
    MondayAvailabilitiesFormset = modelformset_factory(MondaySquedules, form=MondayScheduleForm, extra=0)

    qs = obj.mondaysquedules_set.all()
    formset = MondayAvailabilitiesFormset(queryset=qs)

    context = {'form':form, 'formset':formset}

    if request.method == 'POST':
        form = AgendaForm(request.POST, instance=obj)
        formset = MondayAvailabilitiesFormset(request.POST, queryset=qs)
        if all([form.is_valid(),formset.is_valid()]):
            print('here')
            parent = form.save(commit=False)
            parent.save()    
            for form in formset:
                child = form.save(commit=False)
                child.agenda = parent
                child.save()
            context['message'] = 'Data Saved.'
        if request.htmx:
            return render(request, 'base/partials/forms.html', context)

    return render(request, 'base/test.html', context)










