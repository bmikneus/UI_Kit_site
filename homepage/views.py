from django.shortcuts import render
from django.template.context_processors import csrf
# Create your views here.
def home(request):
    return render(request, 'index.html')