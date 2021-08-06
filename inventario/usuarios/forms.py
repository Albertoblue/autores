from .models import Escritor,Libro
from django.forms import ModelForm


class Autorform(ModelForm):
    class Meta:
        model=Escritor
        fields='__all__'

class Libroform(ModelForm):
    class Meta:
        model=Libro
        fields='__all__'
