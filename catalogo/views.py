from django.shortcuts import render
from catalogo.models import Filme

def catalogo_view(request):
    # Entra no model e pega os objetos que estão dentro dele
    filmes = Filme.objects.all()

    # Criamos um objeto que definimos chaves e valores, e com ela eu vou acessar um valor, e vai levar ate catalogo.html
    contexto = {
        'filmes': filmes
    }
    return render(request, 'catalogo.html', contexto)
