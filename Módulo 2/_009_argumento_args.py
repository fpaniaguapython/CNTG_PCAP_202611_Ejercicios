def conectar(url):
    if len(url.strip())==0:
        raise Exception("Error", 404, "No encontrado")
    print('Conectando...')

try:
    conectar('')
except Exception as ex:
    print(ex.args) # ('Error', 404, 'No encontrado')