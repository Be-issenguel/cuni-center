from django.http import HttpResponse


# Create your views here.
def library_index(request):
    html = "<center><h1>Welcome to MeuGenio</h1></center>"
    return HttpResponse(html)
