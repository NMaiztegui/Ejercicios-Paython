from django import forms
from .models import Ikasle,Ikasgaiak,Notak
class IkasleForm(forms.ModelForm):
 class Meta:
    model=Ikasle
    fields=['izena','abizena','jaiotze_data']

class IkasgaiForm(forms.ModelForm):
  class Meta:
    model=Ikasgaiak
    fields=['izena','maila','hizkuntza']


class NotaForm(forms.ModelForm):
  class Meta:
    model=Notak
    fields=['nota','oharra','Ikasle','Ikasgaiak']

class NoataAldatuForm(forms.ModelForm):
  class Meta:
    model=Notak
    fields=['nota','Ikasle','Ikasgaiak']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Hacer los campos específicos solo lectura
        self.fields['Ikasle'].widget.attrs['readonly'] = 'readonly'  # Campo Ikasle solo lectura
        self.fields['Ikasgaiak'].widget.attrs['readonly'] = 'readonly'  # Campo Ikasgaiak solo lectura