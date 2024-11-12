from django.shortcuts import render

# Create your views here.
# cadastro/views.py
from django.shortcuts import render, redirect
from .forms import UsuarioForm

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = UsuarioForm()
    return render(request, 'hello/cadastrar_usuario.html', {'form': form})
