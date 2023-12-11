from django.shortcuts import render, redirect

from .forms import form_contacto
from django.core.mail import EmailMessage
from django.conf import settings


# Create your views here.

def contacto(request):
    
    formulario_contacto = form_contacto()
    
    if request.method == "POST":
        
        """le decimos que rescate la info del POST y la cargue en el formulario"""
        formulario_contacto = form_contacto(data=request.POST)
        
        if formulario_contacto.is_valid():
            """si el formulario es valido que almacene cada cosa en la variable"""
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')
        
            email_message = EmailMessage("Mensaje enviado de django", "el usuario de nombre {} de correo {} envia lo siguiente: \n\n {}"
                                         .format(nombre,email, contenido), '', ["miguel_kratos@hotmail.com"])
            try:
                email_message.send()
                """luego redirecciono a la pagina para avisar que se envio correctamente la informacion"""
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")            
    
    return render(request, "contacto/contacto.html", {'form_contacto':formulario_contacto} ) 

