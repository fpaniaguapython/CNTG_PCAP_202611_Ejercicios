registro_01 = "20#11#2026#17#22#GRAVE#OR1221"

 
tokens = registro_01.split('#') # Obtener una lista separando por #
print(tokens) # ['20', '11', '2026', '17', '22', 'GRAVE', 'OR1221']

registro = '#'.join(tokens) # Generar un str a partir de la lista utilizando # como separador
print(registro) # 20#11#2026#17#22#GRAVE#OR1221