from django.shortcuts import render
from .models import Entrada
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator


def home(request):
    queryset = request.GET.get("buscar")
    entradas = Entrada.objects.filter(estado='A')
    if queryset:
        posts = Entrada.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion__icontains=queryset)
        ).distinct()
    # paginator = Paginator(entradas, 20)
    # page = request.GET.get('page')
    # entradas = paginator.get_page(page)
    return render(request, 'index.html', {'entradas': entradas})


def detalleEntrada(request, slug):
    # queryset = request.GET.get("buscar")
    entrada = get_object_or_404(Entrada, slug=slug)
    return render(request, 'entrada.html', {'entrada': entrada})
