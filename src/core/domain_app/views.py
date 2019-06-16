from django.shortcuts import render

def index(request):
    return render(request, 'domain_app/index.html')
