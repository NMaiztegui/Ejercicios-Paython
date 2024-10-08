from django import forms
from .models import Kotxea,Bezeroa,AlokatutakoKotxeak

class KotxeForm(forms.ModelForm):
    class Meta:
        model=Kotxea
        fields=['marca','modelo','matricula', ]

class BezeroaForm(forms.ModelForm):
    class Meta:
        model=Bezeroa
        fields=['izena', 'abizena', 'dni']
    
class AlokatuaForm(forms.ModelForm):
    class Meta:
        model=AlokatutakoKotxeak
        fields=['kotxea', 'bezeroa', 'alokatze_data']
    
    def __init__(self, *args, **kwargs):
        super(AlokatuaForm, self).__init__(*args, **kwargs)
        # Filtrar solo coches que no están alquilados
        alquilados_ids = AlokatutakoKotxeak.objects.values_list('kotxea_id', flat=True)
        self.fields['kotxea'].queryset = Kotxea.objects.exclude(id__in=alquilados_ids) #mandar como obciones los kotxes que no estanalquilados, se comprubea si no estan dentro del objeto alquuilados_ids
