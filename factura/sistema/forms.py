from django import forms


class SistemaModelForm(forms.ModelForm):

    def save(self, *args, **kwargs):
        self.instance.sistema = kwargs.pop('sistema')
        return super(SistemaModelForm, self).save(*args, **kwargs)
