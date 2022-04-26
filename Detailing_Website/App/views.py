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


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry" 
            body = {
                'name': form.cleaned_data['name'], 
			    'subject': form.cleaned_data['subject'], 
			    'email': form.cleaned_data['email'], 
			    'message':form.cleaned_data['message'], 
		        }
		    
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'mannyrothwell32@gmail.com', ['mannyrothwell32@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'index.html', {})

    else:
        form = ContactForm()
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def success(request):
    return render(request, 'success.html', {})