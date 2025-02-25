# class - relacion directa con un objeto (entidad o objeto )
# def - acciones o funciones del objeto 

class Personas():
    def __init__(self):
        # atributos del objeto
        self.nombre = "Naudith" # variable de tipo texto "" ''
        self.edad = 30 # variable de tipo numerico 
        self.estatura = 100.0 # variable de tipo decimal 
        self.peso = 35.6  # variable de tipo decimal 


persona =Personas()
print("nombre: ",persona.nombre," edad: ",persona.edad)



