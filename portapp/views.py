from django.shortcuts import render


def port_index(request):
    return render(request, 'portapp/index.html')
