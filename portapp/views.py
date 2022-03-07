from django.shortcuts import render


def port_index(request):
    return render(request, 'portapp/port_index.html')


