'''
 Sirve para crear 
 formularios a partir 
 de los modelos definidos en models.py
'''
from django import forms
'''
Sirve para importar los modelos definidos 
en models.py y poder utilizarlos en los formularios
'''
from .models import *


class FormularioProductos(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__' 
        widgets = {
            'Fecha': forms.DateInput(attrs={'type': 'date'}),
        }