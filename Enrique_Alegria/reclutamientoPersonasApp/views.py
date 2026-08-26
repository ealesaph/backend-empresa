from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

def clientes(request):
    data = {
            'titulo':'Egresados',
            'nombre1': 'Leandro de Miguel',
            'categoria1':'Diseñador/a gráfico/a',
            'desc1':'Excelente experiencia, todo salió perfecto. Muy recomendable.',

            'nombre2': 'Guillermina Miguez',
            'categoria2':'Técnico/a en soporte informático',
            'desc2':'Me encantó el servicio, fueron muy amables y atentos. Sin duda volvería.',
            
            'nombre3': 'Sheila Diallo',
            'categoria3':'Barista',
            'desc3':'Todo estuvo muy bien, superó mis expectativas. ¡Recomendado!',

            'nombre4':'Jessica Molina',
            'categoria4':'Analista de datos',
            'desc4':'Buena atención y excelente calidad. Quedé muy conforme con el resultado.',
            
            'nombre5':'Denis Freire',
            'categoria5':'Fotógrafo/a',
            'desc5':'Una experiencia agradable de principio a fin. El trato fue excelente y todo funcionó como esperaba.',

            'nombre6':'Luz-Maria Mariño',
            'categoria6':'Chef',
            'desc6':'Muy satisfecho con la atención recibida. Se nota el compromiso y la preocupación por entregar un buen servicio.',

            'nombre7':'Maria-Ester Aguilar',
            'categoria7':'Community manager',
            'desc7':'Quedé bastante sorprendido con la calidad. El proceso fue sencillo, rápido y el resultado final cumplió totalmente con lo que necesitaba.',

            'nombre8':'Gerardo Alvarez',
            'categoria8':'Electricista',
            'desc8':'Excelente experiencia. La atención fue cordial, el servicio cumplió con lo prometido y todo se realizó de manera rápida y profesional. Definitivamente lo recomendaría.',

            'nombre9':'Irune Vazquez',
            'categoria9':'Traductor/a',
            'desc9':'Muy buena experiencia en general. Desde el primer momento recibí una atención amable y profesional. Todo fue claro, rápido y sin complicaciones. El resultado superó mis expectativas.',
            
            'nombre10':'Soledad Llanos',
            'categoria10':'Repartidor/a',
            'desc10':'Estoy muy satisfecho con el servicio. La atención fue excelente, el proceso resultó mucho más sencillo de lo esperado y el resultado final fue de muy buena calidad. Sin duda volvería a elegirlos.',
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