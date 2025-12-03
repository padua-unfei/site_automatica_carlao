from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Problema, PerfilOficina, Especialidade


class ClienteSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_cliente = True
        if commit:
            user.save()
        return user

class OficinaSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_oficina = True
        if commit:
            user.save()
        return user

class ProblemaForm(forms.ModelForm):
    class Meta:
        model = Problema
        fields = ['titulo', 'modelo_carro', 'descricao', 'imagem']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo_carro': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class OficinaPerfilForm(forms.ModelForm):
    class Meta:
        model = PerfilOficina
        fields = ['nome_oficina', 'endereco', 'especialidades']
        widgets = {
            'nome_oficina': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidades': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }