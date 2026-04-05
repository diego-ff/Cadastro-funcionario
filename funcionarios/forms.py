from django import forms
from .models import Funcionario


class FuncionarioForm(forms.ModelForm):

    class Meta:

        model = Funcionario

        fields = "__all__"

        widgets = {

            "cpf": forms.TextInput(attrs={
                "placeholder": "000.000.000-00",
                "class": "form-control",
            }),

            "telefone": forms.TextInput(attrs={
                "placeholder": "(14) 99999-9999",
                "class": "form-control",
            }),

            "data_nascimento": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control",
            }),

        }