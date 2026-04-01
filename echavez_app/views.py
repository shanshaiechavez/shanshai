from django.shortcuts import render

def echavez_app(request):
    return render(request, 'designs.html')