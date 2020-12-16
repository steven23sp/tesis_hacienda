from django.shortcuts import render, render_to_response


# Create your views here.
def menu(request):
    data = {
        'title': 'Menu Principal', 'entidad': 'Menu Principal'
    }
    return render(request, '../../sistema_yamaha/templates/prueba/index.html', data)