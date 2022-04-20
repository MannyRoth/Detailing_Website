from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})

def contact(request):
    # if request.method == 'POST':
        
    # else:
    return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})