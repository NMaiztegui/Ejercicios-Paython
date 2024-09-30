from django.shortcuts import render
from.models import Ikasle

def ikasle_list(request):
 ikasleZerrenda=Ikasle.objects.all() #datubastik ikasle .models-ko datu guztiak eskuratu
 return render(request, 'zerrenda/ikasle_list.html', {'ikasleak':ikasleZerrenda})