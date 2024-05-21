import re
import time


# Decorador
def tiempo_ejecucion(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        resultado = func(*args, **kwargs)
        end = time.time()
        print(f'Tiempo de ejecucion: {end - start}')
        return resultado
    return wrapper


@tiempo_ejecucion
def contar_correos_validos(archivo):
    with open(archivo, 'r') as f:
        texto = f.read()
        validacion = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        correos = re.findall(validacion, texto)
        return correos


correos_validos = contar_correos_validos('mails.txt')
print(f'Correos validos encontrados: {len(correos_validos)}')
