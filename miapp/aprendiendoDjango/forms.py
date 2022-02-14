from random import choices
from django import forms

class FormularioArticulo(forms.Form):
    title = forms.CharField(
        label='Titulo'
    )
    contenido = forms.CharField(
         label='Contenido',
         widget=forms.Textarea
    )

    public_options = [(1, 'si'), (2, 'no')]

    publico = forms.TypedChoiceField(
        label='Publico',
        choices= public_options
    )

