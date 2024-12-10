from django import forms
from .models import Autor, Libro, Editorial

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = '__all__'

class BusquedaForm(forms.Form):
    titulo = forms.CharField(max_length=200, required=False)
