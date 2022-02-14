from django import forms
from django.core import validators

class FormularioArticulo(forms.Form):
    title = forms.CharField(
        label='Titulo',
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'pon el titulo',
                'class': 'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'el titulo es demasiado corto'),
            validators.RegexValidator('^[a-Za-z0-9]*$', 'el titulo esta mal formado', 'invalid_title')
        ]
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

