from collections.abc import Mapping
from typing import Any
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.utils import ErrorList
from .models import Servico, CategoriaAdicao

class FormServico(ModelForm):
    class Meta:
        model = Servico
        exclude = ['finalizado', 'protecolo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})
            self.fields[field].widget.attrs.update({'placeholder': field})

        choices = list()
        for i, j in self.fields['categoria_adicao'].choices:
            categoria = CategoriaAdicao.objects.filter(titulo = j).first()
            if categoria:
                choices.append((i.value, categoria.get_titulo_display()))
            else:
                print("banco de dados não contem categorias!")

        self.fields['categoria_adicao'].choices = choices