from django.shortcuts import render,redirect
from.models import Ikasle
from.forms import IkasleForm

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


   