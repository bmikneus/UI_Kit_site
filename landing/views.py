from django.shortcuts import render
from django.template.context_processors import csrf
# Create your views here.
def landing(request):
    return render(request, 'landing-page.html')