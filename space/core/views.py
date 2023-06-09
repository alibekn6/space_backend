from django.shortcuts import render, get_object_or_404
from .models import WhoAreWe, Achivements
# Create your views here.


def index(request):
    whoarewe = WhoAreWe.objects.all()
    achive = Achivements.objects.all()
    return render(request, 'core/index.html', {
        'whoarewe': whoarewe,
        'achive': achive
    })
