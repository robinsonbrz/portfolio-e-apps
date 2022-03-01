from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Contato


def index(request):
    try: 
        contatos = Contato.objects.all()
        return render(request, 'contatos/index.html', {
            'contatos': contatos
        })
    except:
        raise Http404


def ver_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })
