from django.shortcuts import render, render_to_response


# Create your views here.
def menu(request):
    data = {
        'titulo': 'Menu Principal', 'entidad': 'Menu Principal'
    }
    return render(request, 'prueba/index.html', data)