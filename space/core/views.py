from django.shortcuts import render, get_object_or_404
from .models import WhoAreWe
# Create your views here.


def index(request):
    whoarewe = WhoAreWe.objects.all()
    return render(request, 'core/index.html', {
        'whoarewe': whoarewe
    })
