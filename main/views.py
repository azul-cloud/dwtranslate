from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings

from main.models import Experience
from main.forms import ContactForm

def home(request):
    template = "main/content/home.html"
    special_exp = Experience.objects.filter(special=True).order_by('special_order')

    return render(request, template, {'special_exp':special_exp})


def contact(request):
    status=""
    template = "main/content/contact.html"
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            email = EmailMessage('Dennis Wester Translating Contact',
                cd["message"],
                settings.EMAIL_HOST_USER,
                ['awwester@gmail.com'], #dwwester@bossig.com
                headers = {'Reply-To': cd["email"]})
            email.send()

            status = "sent"
            form = ContactForm()

    return render(request, template, {'form':form, 'status':status})


def experience(request):
    template = "main/content/experience.html"
    exp = Experience.objects.all()

    return render(request, template, {'exp':exp})


def about(request):
    template = "main/content/about.html"

    return render(request, template, {})
