import temperatura
import masa 
import tiempo

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen == "celsius" and unidad_destino == "fahrenhe":
        return tiempo.segundo_a_minutos(valor)
    else:
        return None
    
def convertir_masa(valor, unidad_origen, unidad_destino):
    if unidad_origen == "kilogramos" and unidad_destino == "gramos":
        return masa.kilogramos_a_gramos(valor)
    else:
        return None
    
def convertir_tiempo(valor, unidad_origen, unidad_destino):
    if unidad_origen == "segundos" and unidad_destino == "minutos":
        return tiempo.segundo_a_minutos(valor)
    else:
        return None
    
if __name__== "__main__":
    valor = 20
    unidad_origen= "celsius"
    unidad_destino="fahrenheit"
    resultado= convertir_temperatura(valor, unidad_origen, unidad_destino)
    print(f"{valor} de {unidad_origen} son equivalentes a {resultado} {unidad_destino}")

if __name__== "__main__":
    valor = 70
    unidad_origen= "klogramos"
    unidad_destino="gramos"
    resultado= convertir_masa(valor, unidad_origen, unidad_destino)
    print(f"{valor} de {unidad_origen} son equivalentes a {resultado} {unidad_destino}")

if __name__== "__main__":
    valor = 100
    unidad_origen= "segundos"
    unidad_destino="minutos"
    resultado= convertir_tiempo(valor, unidad_origen, unidad_destino)
    print(f"{valor} de {unidad_origen} son equivalentes a {resultado} {unidad_destino}")