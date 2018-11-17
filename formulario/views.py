from django.shortcuts import render
from django.core.mail import send_mail
from formulario.forms import FestForm
from formulario.models import Fest

# Create your views here.


def fest_createview(request):
    if request.method == "POST":
        form = FestForm(request.POST)
        if form.is_valid():
            obj = Fest.objects.create(
                name=form.cleaned_data.get('name'),
                address=form.cleaned_data.get('address'),
                numero=form.cleaned_data.get('numero'),
                email=form.cleaned_data.get('email'),
                option=form.cleaned_data.get('option'),
                allergies=form.cleaned_data.get('allergies')
                )
            subject = 'Winter Acro Festival 2019'
            message = "Hoi " + obj.name + "\r\n\r\nThanks for registering for the Winter Acro Festival 2019!\r\n\r\nLamas are little rebels, they are not good at doing automatic jobs. Definitly not as good as monkeys. Fly better though...\r\n\r\nAnyway, in the next 72 hours you will receive an email concerning your registration status. So just like Axl Rose said: Gotta have some patience.\r\n\r\n\r\nBig Hug\r\nThe Lamas"
            sender = 'notmonkeys@acrofestival.ch'
            to = [obj.email]
            send_mail(subject, message, sender, to)
        if form.errors:
            print(form.errors)
    template_name = 'homeform.html'
    context = {}
    return render(request, template_name, context)
