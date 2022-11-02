from django.shortcuts import render

# Create your views here.
def funcaoView(request):
    return(render(request, 'index.html'))