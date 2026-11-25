peliculas = [('El resplandor', 'Kubrick', 1980), 
             ('Alien','Ridley', 1979), 
             ('Eyes wide shut', 'Kubrick', 1999),
             ('Rondallas', 'Sánchez', 2025)]


def es_de_kubrick(pelicula):
    es_ok = pelicula[1]=='Kubrick'
    return es_ok
# lambda pelicula : pelicula[1]=='Kubrick'

peliculas_de_kubrick = filter(es_de_kubrick, peliculas) # Devuelve un filter
print('Películas de Kubrick')
for pelicula in peliculas_de_kubrick:
    print(pelicula)

peliculas_de_ridley = filter(lambda pelicula : pelicula[1]=='Ridley', peliculas)
print('Películas de Ridley')
for pelicula in peliculas_de_ridley:
    print(pelicula)

# Utilizando funciones lambda, buscar las películas anteriores al año 2000
ANYO_LIMITE = 2000
peliculas_antiguas = filter(lambda pelicula : pelicula[2]<ANYO_LIMITE, peliculas)
peliculas_antiguas = list(peliculas_antiguas)
print(peliculas_antiguas)