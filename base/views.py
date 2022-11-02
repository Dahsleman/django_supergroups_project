from pickle import GET
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
from django.http import Http404, HttpResponse
from django.urls import reverse

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


""" GROUPS"""

def home(request):
    if request.user.is_authenticated: 
        agenda_objects = Agenda.objects.filter(user=request.user)
        current_user = request.user
        groups = Group.objects.filter(participants = current_user)

        group_participants = Group.objects.filter(participants = current_user)

        group_count = groups.count()
        context = {
            'groups': groups, 
            'group_count':group_count, 
            'group:participants':group_participants,
            'agenda_objects':agenda_objects
            }
        return render(request, 'base/home.html', context)
    else:
        return redirect('register')   

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

""" PROFILE """

def userProfile(request, pk):
    agenda_objects = Agenda.objects.filter(user=request.user)
    users = User.objects.get(id=pk)

    context = {
        'users':users,
        'agenda_objects':agenda_objects,
        }
    return render(request, 'base/user_profile.html', context)


""" AUTH """
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


"""SETTINGS"""

def telegram(request):
    """telegram-agenda-list"""
    agenda_objects = Agenda.objects.filter(user=request.user)

    context = {
        'agenda_objects':agenda_objects,
    }
    return render(request, 'base/telegram.html', context)



def telegramSettingsOH(request):
    current_user = request.user
    objects = Settings.objects.filter(user=current_user)
    OH_objects = Settings.objects.get(user=current_user)
    agenda_objects = Agenda.objects.filter(user=request.user)
    status = OH_objects.status
    time = OH_objects.time
    permanently_closed = 'permanently closed'
    set_open_and_close_time = 'set open and close time'

    context = {
        'objects':objects, 
        'status':status, 
        'permanently_closed':permanently_closed, 
        'set_open_and_close_time':set_open_and_close_time, 
        'time':time,
        'agenda_objects':agenda_objects,
    }
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
    agenda_objects = Agenda.objects.filter(user=request.user)
    hx_url = reverse("hx-telegram-agenda-detail", kwargs={"id": id})
    context = {
        'hx_url':hx_url,
        'agenda_objects':agenda_objects,
    }
    return render(request, 'base/telegram-agenda-detail.html', context)

@login_required
def telegramAgenda_detail_hx(request, id):
    agenda_objects = Agenda.objects.filter(user=request.user)
    num = str(agenda_objects.count())
    if not request.htmx:
        raise Http404
    try:
        agenda_obj = Agenda.objects.get(id=id, user=request.user)
        monday=agenda_obj.monday
    except:
        agenda_obj = None
    if agenda_obj is None:
        return HttpResponse('Not found.')
    
    context = {
        'agenda_obj':agenda_obj,
        'agenda_objects':agenda_objects,
        'num':num,
        'monday':monday
    }
    return render(request, 'base/partials/telegram-agenda-detail.html', context)


@login_required
def telegramAgenda_delete(request, id=None):
    agenda_objects = Agenda.objects.filter(user=request.user)

    try:
        agenda_obj = get_object_or_404(Agenda, id=id, user=request.user)
    except:
        agenda_obj = None
    if agenda_obj is None:
        if request.htmx:
            return HttpResponse('Not found')
        raise Http404
    
    if request.method == "POST":
        agenda_obj.delete()

        success_url = reverse('telegram-agenda-list')
        if request.htmx:
            headers = {
                'HX-Redirect':success_url
            }
            return HttpResponse('Success',headers=headers)
        return redirect(success_url)

    context = {
        
        'agenda_objects':agenda_objects,
        'agenda_obj':agenda_obj,
    }
    return render(request, 'base/telegram-agenda-delete.html', context)


@login_required
def telegramAgenda_update(request, id=None):
    agenda_objects = Agenda.objects.filter(user=request.user)
    agenda_obj = get_object_or_404(Agenda, id=id, user=request.user)
    children_obj = agenda_obj.get_monday_schedules_children()
    quantity = str(children_obj.count())
    form = AgendaForm(request.POST or None, instance=agenda_obj)
    new_monday_url = reverse("hx-monday-create", kwargs={"parent_id":agenda_obj.id})

    true = True
    context = {
        'true':true,
        'agenda_objects':agenda_objects,
        'new_monday_url':new_monday_url,

        'form':form,
        'agenda_obj':agenda_obj,

        'quantity':quantity
        
        }

    if form.is_valid():
        parent=form.save(commit=False)
        display_type = request.POST.get("display-type", None)
        if display_type in ["mondaybox"]:
            if quantity > '0':
                parent.monday = True
            else:
                context['error'] = 'Insert squedule'
                return render(request, 'base/partials/forms.html', context)

        else:
            parent.monday = False
        parent.save()
        context['message'] = 'Data saved.'

        if request.htmx:
            headers = {
                "HX-Redirect": parent.get_absolute_url(),
            }
            return HttpResponse("Created", headers=headers)
        return redirect(parent.get_absolute_url())

    return render(request, 'base/telegram-agenda-create-update.html', context)

@login_required
def telegramAgenda_create(request):
    agenda_objects = Agenda.objects.filter(user=request.user)
    form = AgendaForm(request.POST or None)
    context = {
        'form':form,
        'agenda_objects':agenda_objects,
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        if request.htmx:
            headers = {
                "HX-Redirect": obj.get_absolute_url(),
            }
            return HttpResponse("Created", headers=headers)
        return redirect(obj.get_absolute_url())
    return render(request, 'base/telegram-agenda-create-update.html', context)

@login_required
def telegramMonday_update_hx(request, parent_id=None, id=None):

    if not request.htmx:
        raise Http404
    try:
        parent_agenda_obj = Agenda.objects.get(id=parent_id, user=request.user)
    except:
        parent_agenda_obj = None

    if parent_agenda_obj is None:
        return HttpResponse('Not found.')
        
    instance = None
    if id is not None:
        try:
            instance = MondaySquedules.objects.get(agenda=parent_agenda_obj, id=id)
        except:
            instance = None

    form = MondayScheduleForm(request.POST or None, instance=instance)

    url = reverse ("hx-monday-create", kwargs={"parent_id":parent_agenda_obj.id})
    if instance:
        url = instance.get_hx_edit_url()

    context = {
        'object':instance,
        'form':form,
        'url':url,
    }

    if form.is_valid():
        new_obj = form.save(commit=False)
        start_list=[]
        end_list=[]
        user_id=request.user.id
        objs=MondaySquedules.objects.filter(agenda__user__id=user_id)
        for obj in objs:
            start_list.append(obj.start_time)
            end_list.append(obj.end_time)

        if instance is None:
        
            if int(new_obj.start_time) > int(new_obj.end_time):
                start_list.clear()
                end_list.clear()
                error='end time must be bigger'
                context['error'] = error
                return render(request, 'base/partials/monday-form.html', context)

            num = len(start_list)
            if num > 0:
                while num != 0:
                    num = num - 1
                    if int(new_obj.start_time) >= int(start_list[num]) and int(new_obj.start_time) < int(end_list[num]):
                        start_list.clear()
                        end_list.clear()
                        error='conflict, select a diferent start time'
                        context['error'] = error
                        return render(request, 'base/partials/monday-form.html', context)
                    elif int(new_obj.end_time) > int(start_list[num]) and int(new_obj.end_time) <= int(end_list[num]):
                        start_list.clear()
                        end_list.clear()
                        error='conflict, select diferent end time'
                        context['error'] = error
                        return render(request, 'base/partials/monday-form.html', context)
                    elif int(new_obj.start_time) < int(start_list[num]) and int(new_obj.end_time) > int(end_list[num]):
                        start_list.clear()
                        end_list.clear()
                        error='conflict, select diferent interval'
                        context['error'] = error
                        return render(request, 'base/partials/monday-form.html', context)

            new_obj.agenda = parent_agenda_obj
        new_obj.save()
        start_list.clear()
        end_list.clear()

        context['object'] = new_obj

        return render(request, 'base/partials/monday-inline-del.html', context)
        
    return render(request, 'base/partials/monday-form.html', context)

@login_required
def telegramMonday_delete(request, parent_id=None, id=None):
    # agenda_objects = Agenda.objects.filter(user=request.user)
    monday_obj = get_object_or_404(MondaySquedules, agenda__id=parent_id, id=id, agenda__user=request.user)
    monday_obj.delete()
    success_url = reverse('telegram-agenda-update', kwargs={'id':parent_id})
    return redirect(success_url)

"""Test"""

def testUpdate(request):
    pass

    return render(request, 'base/test.html')










