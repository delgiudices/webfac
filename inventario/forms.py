from .models import Articulo
from sistema.forms import SistemaModelForm


class ArticuloForm(SistemaModelForm):

    def __init__(self, *args, **kwargs):
        super(ArticuloForm, self).__init__(*args, **kwargs)
        self.fields['cantidad'].required = False

    class Meta:
        model = Articulo
        exclude = ['sistema', 'codigo']
