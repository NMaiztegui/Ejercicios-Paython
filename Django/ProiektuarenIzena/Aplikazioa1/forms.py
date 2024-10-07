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
        super(NoataAldatuForm,self).__init__(*args, **kwargs)
        if self.instance:
         
          self.fields['Ikasle'].disabled = True 
          self.fields['Ikasgaiak'].disabled = True  