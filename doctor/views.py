from django.shortcuts import render

def front(request):
    return render(request, 'doctor/clinic.html')

def contact(request):
    return render(request, 'doctor/contact.html')

def services(request):
    return render(request, 'doctor/services.html')

def providers(request):
    return render(request, 'doctor/provider.html')