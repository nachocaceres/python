from django import forms

class ClaseFormulario(forms.Form):

    clase = forms.CharField()
    fecha = forms.IntegerField()