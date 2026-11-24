import dataclasses

class Pelicula:
    def __init__(self, titulo, director):
        self.titulo = titulo
        self.director = director

    def __str__(self) -> str:
        #return f'Título:{self.titulo}. Director:{self.director}'
        return str(self.__dict__)

    # Si no existe __str__ se ejecuta __repr__
    # Es el utilizado cuando el objeto está en una estructura tipo lista, tupla, etc.
    def __repr__(self) -> str:
        # return str(self.__dict__) # Opción 1, programar un comportamiento propio
        return self.__str__() # Opción 2, devolver lo que devuelve __str__

alien = Pelicula('Alien', 'Ridley Scott')
batman = Pelicula('Batman', 'Tim Burton')

peliculas = [alien, batman]

print(alien) # (sin __str__) <__main__.Pelicula object at 0x0000023817598980>
print(alien) # (con __str__) Título:Alien. Director:Ridley Scott
print(alien) # (con __str__ devolviendo __dict) {'titulo': 'Alien', 'director': 'Ridley Scott'}

print(peliculas) # (sin __repr__) [<__main__.Pelicula object at 0x00000229A59D8980>, <__main__.Pelicula object at 0x00000229A59B8410>]
print(peliculas) # (con __repr__) [{'titulo': 'Alien', 'director': 'Ridley Scott'}, {'titulo': 'Batman', 'director': 'Tim Burton'}]