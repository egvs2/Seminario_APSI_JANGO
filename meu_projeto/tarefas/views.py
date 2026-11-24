from django.shortcuts import get_object_or_404, redirect, render
from .models import Tarefa


def listar(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'listar.html', {'tarefas': tarefas})


def criar(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo', '').strip()
        if titulo:
            Tarefa.objects.create(titulo=titulo)
        return redirect('listar')
    return render(request, 'criar.html')


def editar(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    if request.method == 'POST':
        titulo = request.POST.get('titulo', '').strip()
        if titulo:
            tarefa.titulo = titulo
        tarefa.concluida = 'concluida' in request.POST
        tarefa.save()
        return redirect('listar')
    return render(request, 'editar.html', {'tarefa': tarefa})


def excluir(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('listar')
    return render(request, 'excluir.html', {'tarefa': tarefa})