from django.shortcuts import render
from .models import Member

# Create your views here.

def spaceteam(request):
    members = Member.objects.all()
    return render(request, 'team/team.html', {
        'members': members
    })