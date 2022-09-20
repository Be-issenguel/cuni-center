from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def library_index(request):

    html = "<center><h1>Welcome to MeuGenio</h1></center>"
    context = {}
    return render(request, 'frontend/coming-soon.html', context=context)
