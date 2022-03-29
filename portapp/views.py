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
