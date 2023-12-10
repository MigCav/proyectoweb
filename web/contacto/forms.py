from django import forms

class form_contacto(forms.Form):
    
    nombre = forms.CharField(label= 'Nombre', required=True)
    email  = forms.CharField(label='Email', required=True)
    contenido = forms.CharField(label='Contenido', widget=forms.Textarea)
    