
from base.models import *
from django.shortcuts import render

def agenda_view(request):
    agenda_objects = Agenda.objects.filter(user=request.user)
    print('here')
    context = {
        'agenda_objects':agenda_objects,
    }
    return render(request, 'main.html', context)