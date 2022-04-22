from django.http import HttpResponse
from django.shortcuts import render
from itsdangerous import BadHeader
from service_identity import SubjectAltNameWarning
from django import forms
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        name = request.POST ['name']
        subject = request.POST ['subject']
        email = request.POST ['email']
        message = request.POST ['message']
        try:
            send_mail(subject, message, email, ['mannyrothwell32@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

    else:
        form = ContactForm()
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def success(request):
    return render(request, 'success.html', {})