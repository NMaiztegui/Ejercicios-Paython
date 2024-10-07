from django.shortcuts import render,redirect
from django.db.models import Q 
from django.contrib import messages
from.models import Ikasle,Ikasgaiak,Notak
from.forms import IkasleForm, IkasgaiForm,NotaForm,NoataAldatuForm

def ikasle_list(request):
 ikasleZerrenda=Ikasle.objects.all() #datubastik ikasle .models-ko datu guztiak eskuratu
 return render(request, 'zerrenda/ikasle_list.html', {'ikasleak':ikasleZerrenda})

def ikasle_new(request):
    #al principio muestra un formulario vacio, cuando se le de a sumit es cuando se ejecuta el metodo sumit y manda los datos a la base de datos, y nos redirecciona a a la pagina principla
    if request.method == 'POST':
        form=IkasleForm(request.POST)
        if form.is_valid:
            ikasle = form.save()
            ikasle.save()
        return redirect('zerrenda-default') #cuandoi los datos se guardan y se meten al servidor, vulev a enviar al la vista inicila
    else:
        form=IkasleForm()
        return render(request, 'zerrenda/ikasle_new.html', {'form':form})


def ikasgai_list(request):
    ikasgaiZerrenda=Ikasgaiak.objects.all() #datubastik ikasle .models-ko datu guztiak eskuratu
    return render(request, 'zerrenda/ikasgaiak_list.html', {'ikasgaiak':ikasgaiZerrenda})

def ikasgai_new(request):
    if request.method == 'POST':
        form=IkasgaiForm(request.POST)
        if form.is_valid:
            ikasgai = form.save()
            ikasgai.save()
        return redirect('zerrenda-ikasgaiak') #cuandoi los datos se guardan y se meten al servidor, vulev a enviar al la vista inicila
    else:
        form=IkasgaiForm()
        return render(request, 'zerrenda/ikasgai_new.html', {'form':form})

def notak_list(request):
    notak_zerrenda=Notak.objects.all()
    return render(request, 'zerrenda/notak_list.html', {'notak': notak_zerrenda})


def notak_new(request): 
    if request.method == 'POST':
        form = NotaForm(request.POST)
        
        if form.is_valid():  # Validar los datos sin guardarlos
            nueva_nota = form.cleaned_data.get('nota')  # Obtener la nota del formulario
            alumno = form.cleaned_data.get('Ikasle')    # Obtener el alumno del formulario
            asignatura = form.cleaned_data.get('Ikasgaiak')  # Obtener la asignatura del formulario
            
            # Comprobar si ya existe una nota para este alumno y asignatura
            nota_existe = Notak.objects.filter(
                Q(Ikasle=alumno) & Q(Ikasgaiak=asignatura)
            ).exists()

            if nota_existe:
                # Si ya existe una nota similar, muestra un error
                form.add_error('nota', 'Ya existe una nota para este alumno en esta asignatura.')
            elif nueva_nota > 10:
                # Validar si la nota es mayor a 10
                form.add_error('nota', 'La nota no puede ser mayor que 10.')
            elif nueva_nota <= 10:
                # Si todo está bien, guardar la nueva nota
                form.save()
                return redirect('zerrenda-notak')  # Redirigir a la vista inicial después de guardar

        # Si no es válido o hay algún error, volver a mostrar el formulario con los errores
        return render(request, 'zerrenda/notak_new.html', {'form': form})

    else:
        form = NotaForm()  # Si no es un POST, mostrar un formulario vacío
    
    return render(request, 'zerrenda/notak_new.html', {'form': form})




def nota_aldatu(request,kod_ikaslea,kod_ikasgaia):
    nota=Notak.objects.get(Ikasle_id=kod_ikaslea,Ikasgaiak_id=kod_ikasgaia) #coger los id asignado al ikasle y su nota
    print(nota)
    form=NoataAldatuForm(request.POST,instance=nota)
    if request.method=='POST':
        
        if form.is_valid():
             nota_berria=form.save()
             nota_berria.save()
        return redirect('zerrenda-notak' )
    else:
        form=NoataAldatuForm(instance=nota)
        return render(request,'zerrenda/aldatu_nota.html', {'form':form})

def nota_ezabatu(request,kod_ikaslea,kod_ikasgaia):
    nota=Notak.objects.get(Ikasle_id=kod_ikaslea,Ikasgaiak_id=kod_ikasgaia) #coger los id asignado al ikasle y su nota
    print(nota)
    if request.method=='POST':
        nota.delete()
        messages.success(request,'Nota ezabatua')
        return redirect('zerrenda-notak')

def ikaslea_ezabatu(request,kod_ikaslea):
    ikaslea=Ikasle.objects.get(id=kod_ikaslea)
    print(ikaslea)
    if request.method=='POST':
        ikaslea.delete()
        messages.success(request,'Ikaslea ezabatua')
        return redirect('zerrenda-default')