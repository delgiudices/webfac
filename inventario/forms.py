from django import forms
from .models import Articulo


class ArticuloForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ArticuloForm, self).__init__(*args, **kwargs)
        self.fields['cantidad'].required = False

    def save(self, **kwargs):
        articulo_fields = kwargs.copy()

        if self.cleaned_data['cantidad'] is None:
            self.cleaned_data.pop('cantidad')

        articulo_fields.update(self.cleaned_data)
        return Articulo.objects.create(**articulo_fields)

    class Meta:
        model = Articulo
        exclude = ['sistema', 'codigo']
