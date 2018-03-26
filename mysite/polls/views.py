from django.shortcuts import render
from .models import Poem

# Create your views here.
def home(request):
    poems = Poem.objects.all()
    return render(request, 'home.html', context=locals())

