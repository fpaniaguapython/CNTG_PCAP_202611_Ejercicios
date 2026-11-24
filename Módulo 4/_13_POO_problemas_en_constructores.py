class Curriculum:
    #def __init__(self, nombre: str, idiomas: list):# Problemático
    def __init__(self, nombre: str): # Solución
        self.nombre = nombre
        self.idiomas = []

    def agregar_idioma(self, idioma):
        self.idiomas.append(idioma)

    def __str__(self):
        return str(self.__dict__)

#lista_idiomas=[] # Problemático
#cv_daniel = Curriculum('Daniel', lista_idiomas) # Problemático
#cv_estrella = Curriculum('Estrella', lista_idiomas) # Problemático

cv_daniel = Curriculum('Daniel') # Solución
cv_estrella = Curriculum('Estrella') # Solución

cv_daniel.agregar_idioma('Japonés')
cv_daniel.agregar_idioma('Italiano')

print(cv_daniel) # {'nombre': 'Estrella', 'idiomas': ['Japonés', 'Italiano']}
print(cv_estrella) # {'nombre': 'Estrella', 'idiomas': ['Japonés', 'Italiano']}