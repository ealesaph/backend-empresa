from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

def clientes(request):
    data = {
            'titulo':'Egresados',
            'nombre1': '',
            'categoria1':'',
            'desc1':'',
            'nombre2': '',
            'categoria2':'',
            'desc2':'',
            'nombre3': '',
            'categoria3':'',
            'desc3':'',
            'nombre4':'',
            'categoria4':'',
            'desc4':'',
            'nombre5':'',
            'categoria5':'',
            'desc5':'',
            'nombre6':'',
            'categoria6':'',
            'desc6':'',
            'nombre7':'',
            'categoria7':'',
            'desc7':'',
            'nombre8':'',
            'categoria8':'',
            'desc8':'',
            'nombre9':'',
            'categoria9':'',
            'desc9':'',
            'nombre10':'',
            'categoria10':'',
            'desc10':'',
        }
    return render(request,'clientes.html',{})

def egresados(request):
    data = {
            'titulo':'Egresados',
            'nombre1': '',
            'categoria1':'',
            'desc1':'',
            'nombre2': '',
            'categoria2':'',
            'desc2':'',
            'nombre3': '',
            'categoria3':'',
            'desc3':'',
            'nombre4':'',
            'categoria4':'',
            'desc4':'',
            'nombre5':'',
            'categoria5':'',
            'desc5':'',
            'nombre6':'',
            'categoria6':'',
            'desc6':'',
            'nombre7':'',
            'categoria7':'',
            'desc7':'',
            'nombre8':'',
            'categoria8':'',
            'desc8':'',
        }
    return render(request,'egresados.html', {})

def personal(request):
    data = {
        'titulo':'Personal',
        'nombre1': '',
        'categoria1':'',
        'desc1':'',
        'nombre2': '',
        'categoria2':'',
        'desc2':'',
        'nombre3': '',
        'categoria3':'',
        'desc3':'',
        'nombre4':'',
        'categoria4':'',
        'desc4':'',
        'nombre5':'',
        'categoria5':'',
        'desc5':'',
    }
    return render(request, 'personal.html', {})