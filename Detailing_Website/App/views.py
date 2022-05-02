from django.http import HttpResponse
from django.shortcuts import render
from itsdangerous import BadHeader
from service_identity import SubjectAltNameWarning
from django import forms
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm



def index(request):
    return render(request, 'index.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})


def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject= request.POST.get('subject')
        message = request.POST.get('message')
    
        data = { 
                'name': name,
                'email': email,
                'subject': subject,
                'message': message
        }
        message = ''' 
        Subject: {}
        Message: {}
        From: {}
        Email: {}
        '''.format(data['subject'], data['message'], data['name'], data['email'])

        send_mail(data['subject'], message, '', ['mannyrothwell32@gmail.com'])
        
            
        return render(request, 'sent.html', {})

    else:
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def sent(request):
    return render(request, 'sent.html', {})
