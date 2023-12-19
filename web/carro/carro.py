class Carro:
    def __init__(self):
        self.request = request
        
        #se mantiene el id de la sesion
        self.session = request.session      
        carro = self.session.get('carro')
        
        if not carro:
            #si no hay carro crea uno nuevo con un diccionario vacio
            carro = self.session['carro']= {}
        else:
            #si hay carro en la sesion lo recupera
            self.carro = carro
            
            
    def agregar(self, producto):
        #se verifica si el id del producto no esta en las claves del diccionario
        if (str(producto.id) not in self.carro.keys()):
            #especifico lo que se mostrara en el carrito
            self.carro[producto.id]= {
                'producto_id':producto.id,
                'nombre': producto.nombre,
                'precio': str(producto.precio),
                'cantidad':1,
                'imagen': producto.imagen.url
            }
        else:
            for key,value in self.carro.items():
                if key == str(producto.id):
                    value['cantidad'] = value['cantidad']+1
                    break
                
        self.guardar_carro
        
    def guardar_carro(self):
        self.session['carro'] = self.carro
        self.session.modified = True
        
    def eliminar(self,producto):
        producto.id = str(producto.id)
        if producto.id in self.carro():
            del self.carro[producto]
            self.guardar_carro()
            
    def restar_productos(self, producto):
        #recorremos los valores del diccionario para encontrar el producto
        for key,value in self.carro.items():
            if key == str(producto.id):
                #le restamos 1 a la cantidad
                value['cantidad'] = value['cantidad']-1
                #si el valor es menor a 1 se elimina el producto
                if value['cantidad'] <1:
                    self.eliminar(producto)
                break
            
        self.guardar_carro()
            
    def limpiar_carro(self):
        self.session['carro'] = {}
        self.session.modified = True