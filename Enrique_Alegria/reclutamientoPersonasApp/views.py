from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

def clientes(request):
    data = {
            'titulo':'Egresados',
            'nombre1': 'Leandro de Miguel',
            'categoria1':'',
            'desc1':'',

            'nombre2': 'Guillermina Miguez',
            'categoria2':'',
            'desc2':'',
            
            'nombre3': 'Sheila Diallo',
            'categoria3':'',
            'desc3':'',

            'nombre4':'Jessica Molina',
            'categoria4':'',
            'desc4':'',
            
            'nombre5':'Denis Freire',
            'categoria5':'',
            'desc5':'',

            'nombre6':'Luz-Maria Mariño',
            'categoria6':'',
            'desc6':'',

            'nombre7':'Maria-Ester Aguilar',
            'categoria7':'',
            'desc7':'',

            'nombre8':'Gerardo Alvarez',
            'categoria8':'',
            'desc8':'',

            'nombre9':'Irune Vazquez',
            'categoria9':'',
            'desc9':'',
            
            'nombre10':'Soledad Llanos',
            'categoria10':'',
            'desc10':'',
        }
    return render(request,'clientes.html', data)

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
    return render(request,'egresados.html', data)

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
    return render(request, 'personal.html', data)