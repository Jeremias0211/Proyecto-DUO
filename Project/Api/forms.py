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
            'Precio': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'Cantidad': forms.NumberInput(attrs={'min': '0'}),
            'Descripcion': forms.Textarea(attrs={'rows': 3}),
            'Fecha': forms.DateInput(attrs={'type': 'date'}),
            'Imagen': forms.ClearableFileInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            w = field.widget
            if isinstance(w, forms.CheckboxInput):
                continue
            w.attrs['class'] = (w.attrs.get('class', '') + ' form-control').strip()
        if self.is_bound and self.errors:
            for name in self.errors:
                if name not in self.fields:
                    continue
                w = self.fields[name].widget
                w.attrs['class'] = (w.attrs.get('class', '') + ' is-invalid').strip()