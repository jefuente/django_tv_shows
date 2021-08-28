from django.shortcuts import render, redirect
from app.models import Show
from django.contrib import messages

def index(request):
    return redirect("/shows")

def shows(request):
    context = {
        'programas_tv' : Show.objects.all(),
    }
    return render(request, 'shows.html', context)

def agregar(request):
    context = {
        
    }
    return render(request, 'agregar.html', context)

def editar(request, id):
    context = {
        'id' : id,
        'prog': Show.objects.get(id=id),
    }
    return render(request, 'editar.html', context)
    

def show(request, id):
    context = {
        'id' : id,
        'programa' : Show.objects.get(id=id),
    }
    return render(request, 'mostrar.html', context)


def crear_show(request):
    print(request.POST)

    errores = Show.objects.validador(request.POST)
    print(errores)

    if len(errores) > 0:
        # si el diccionario de errores contiene algo, recorra cada par clave-valor y cree un mensaje flash
        for key, value in errores.items():
            messages.error(request, value)

        request.session['crear_title']=request.POST['title']
        request.session['crear_network']=request.POST['network']
        request.session['crear_release']=request.POST['release']
        request.session['crear_description']=request.POST['description']  

        # redirigir al usuario al formulario para corregir los errores
        return redirect("/shows/new")
    else:
        request.session['crear_title']=""
        request.session['crear_network']=""
        request.session['crear_release']=""
        request.session['crear_description']=""

        show = Show.objects.create(
                title=request.POST['title'],
                network=request.POST['network'],
                release_date=request.POST['release'],
                description=request.POST['description'],  
            )

        messages.success(request,"Exito en agregar el título "+show.title)
    return redirect(f"/shows/{show.id}")

def update(request, id):
    print(request.POST)

    errores = Show.objects.validador(request.POST)
    print(errores)

    if len(errores) > 0:
        # si el diccionario de errores contiene algo, recorra cada par clave-valor y cree un mensaje flash
        for key, value in errores.items():
            messages.error(request, value)

        context = {
        'id' : id,
        'prog': Show.objects.get(id=id),
        }

        request.session['editar_title']=request.POST['title']
        request.session['editar_network']=request.POST['network']
        request.session['editar_release']=request.POST['release']
        request.session['editar_description']=request.POST['description'] 

        # redirigir al usuario al formulario para corregir los errores
        return render(request, 'editar.html', context)

    else:

        request.session['editar_title']=''
        request.session['editar_network']=''
        request.session['editar_release']=''
        request.session['editar_description']=''

        tv_show = Show.objects.get(id=request.POST['identificador'])
        tv_show.title=request.POST['title']
        tv_show.network=request.POST['network']
        tv_show.release_date=request.POST['release']
        tv_show.description=request.POST['description'] 
        tv_show.save()
        messages.success(request,"Exito en editar el título "+tv_show.title)
        return redirect(f"/shows/{tv_show.id}")

def borrar(request, id):
    id : id
    programa = Show.objects.get(id=id)
    programa.delete()
    messages.success(request,"Exito en eliminar el título "+programa.title)
    return redirect("/shows")
