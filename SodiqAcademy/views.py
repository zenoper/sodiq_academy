# yourapp/views.py

from django.shortcuts import render

def landing_page(request):
    return render(request, 'SodiqAcademy/index.html')