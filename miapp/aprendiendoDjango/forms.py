from turtle import textinput
from django import forms

class FormularioArticulo(forms.Form):
    title = forms.CharField(
        label='Titulo',
        # otros atributos
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'pon el titulo',
                'class': 'titulo_form_article'
            }
        )
    )

    content = forms.CharField(
         label='Contenido',
         widget=forms.Textarea
    )

    public_options = [(1, 'si'), (2, 'no')]

    public = forms.TypedChoiceField(
        label='Publico',
        choices= public_options
    )

