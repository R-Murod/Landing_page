from datetime import datetime

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from main.models import *


def home(request):
    users = Email.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        surname = request.POST.get('surname', '')

        if email:
            subscriber = Email.objects.filter(email=email)
            if not subscriber:
                subscriber = Email()
                subscriber.email = email
                subscriber.name = name
                subscriber.surname = surname
                subscriber.sent_at = datetime.now()
                subscriber.save()

        data = {
            'name': name,
            'email': email,
            'surname': surname,
        }
        email_text = f'Ближайшие дни мы вам звоним {name}'
        print(data)
        send_mail(data['name'] + ", спасибо за подписку!", email_text, '', [data['email']])
        return redirect('/')
    return render(request, "index.html", {'users': users})
