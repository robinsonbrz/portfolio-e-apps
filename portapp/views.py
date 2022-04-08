import email.message
import os
import smtplib

from django.http import HttpResponse
from django.shortcuts import render


def inicio(request):
    return render(request, 'portapp/index.html')


def about(request):
    return render(request, 'portapp/about.html')


def expertise(request):
    return render(request, 'portapp/expertise.html')


def portfolio(request):
    return render(request, 'portapp/portfolio.html')


def contato(request):
    return render(request, 'portapp/contato.html')


def ajxmail(request):
    name = request.POST["name"]
    email_contato = request.POST["email"]
    subject = request.POST["subject"]
    message = request.POST["message"]
    print(name, email, subject, message, "Antes chamada email")
    envia_email(name, email_contato, subject, message)
    return HttpResponse('OK')


def envia_email(name, email_contato, subject, message):
    corpo_email = f"""
        <p>Obrigado pelo Contato<b> {name}</b>!</p>
        <p><b>Assunto:</b></p>
        <p> <i>{subject}</i></p>
        <p><b>Mensagem:</b></p>
        <p> <i>{message}</i></p>
        <br>
        <p>Em breve você receberá uma resposta.</p>
        <br>
        <p>Uma ótima semana, </p>
        <br>
        <p><b>Robinson Enedino</b></p>
        <p>Enedino.com.br</p>
    """
    msg = email.message.Message()
    msg['Subject'] = f"Enedino.com.br - {name} - {subject}"
    msg['From'] = "robinsonbrz@gmail.com"
    # msg['To'] = 'robinsonbrz@gmail.com'
    msg['To'] = f'{email_contato}, robinsonbrz@gmail.com'
    GMAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD', 'INSECURE')
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], GMAIL_PASSWORD)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
