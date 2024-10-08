from django.shortcuts import render,redirect
from django.db.models import Q 
from .models import Kotxea,Bezeroa,AlokatutakoKotxeak
from.forms import KotxeForm,BezeroaForm,AlokatuaForm

def main_page(request):
    return render(request,'hasiera.html')


def kotxe_list(request):
   # Obtener todos los coches
    kotxeak = Kotxea.objects.all()

    


    return render(request,'zerrenda/kotxe_list.html', {'kotxeak':kotxeak})

def kotxe_new(request):
    #al principio muestra un formulario vacio, cuando se le de a sumit es cuando se ejecuta el metodo sumit y manda los datos a la base de datos, y nos redirecciona a a la pagina principla
    if request.method=='POST':
        form=KotxeForm(request.POST)
        if form.is_valid():
            kotxea=form.save()
            kotxea.save()
        return redirect('kotxe-zerrenda')
    else:
        form=KotxeForm()
        return render(request,'formularioak/kotxea_new.html', {'form':form})#cuandoi los datos se guardan y se meten al servidor, vulev a enviar al la vista inicila

def bezeroa_list(rquest):
    bezeroak=Bezeroa.objects.all()
    return render(rquest, 'zerrenda/bezero_list.html', {'bezeroak':bezeroak})

def bezeroa_new(request):
    if request.method =='POST':
        form=BezeroaForm(request.POST)
        if form.is_valid():
            bezeroa=form.save()
            bezeroa.save()
        return redirect('bezeroak-zerrenda')
    else:
        form=BezeroaForm
        return render(request, 'formularioak/bezero_berria.html', {'form':form})

# def alokatuak_new(request):
#     if request.method=='POST':
#         form=AlokatuaForm(request.POST)
#         if form.is_valid(): 
#             alokatu=form.save()
#             alokatu.save()
#         return redirect('alokatuak-zerrenda')
#     else:
#         form=AlokatuaForm
#         return render(request, 'formularioak/alokatua_new.html', {'form':form})

def alokatuak_list(rquest):
    alokatuak=AlokatutakoKotxeak.objects.all()
    return render(rquest, 'zerrenda/alokatuak_list.html', {'kotxeak':alokatuak})

def alokatuak_new(request):
    if request.method=='POST':
        form=AlokatuaForm(request.POST)
        if form.is_valid():
                
            aukeratutako_kotxea= form.cleaned_data.get('kotxea')
            # Actualizar el estado del coche a alquilado
            kotxea = Kotxea.objects.get(id=aukeratutako_kotxea.id)
            kotxea.alokatua = True  # Establecer alokatua a True
            kotxea.save()  # Guardar el cambio en la base de datos

            alokatu=form.save()
            alokatu.save()
        return redirect('alokatuak-zerrenda')
    else:
        form=AlokatuaForm
        return render(request, 'formularioak/alokatua_new.html', {'form':form})
    



      
        
       

      