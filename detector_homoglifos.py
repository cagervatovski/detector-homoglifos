# Detector de homoglifos v1.0
# Analiza el dominio de un mail o una URL y marca los caracteres no ASCII
# (por ejemplo, letras cirílicas que imitan letras latinas).
import unicodedata

# Conjuntos de caracteres considerados normales.
# Todo lo que no esté en ninguno se clasifica como "Raro".
alfa= set("abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ") 
num=set("0123456789")
espe=set(" ") 
simbol=set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~¿¡´¨') 

# Tabla de equivalencias: carácter cirílico -> letra latina a la que se parece.
parecidos = {"а": "a", "р": "p", "у": "y"}

def clasificar(caracter):
    # Devuelve el tipo de un carácter: Letra, Numero, Espacio, Simbolo o Raro.
    if caracter in alfa:
        return "Letra"
    elif caracter in num:
        return "Numero"
    elif caracter in espe:
        return "Espacio"
    elif caracter in simbol:
        return "Simbolo"
    else:
        return "Raro"

def analizar(texto_verificar):
    # Cuenta los caracteres por tipo y guarda los raros con su posición.
    # Devuelve (diccionario de contadores, lista de tuplas (posición, carácter)).
    contadores={"Letra":0, "Numero":0, "Espacio": 0, "Simbolo": 0,"Raro":0}
    raros=[]
    for pos,i in enumerate(texto_verificar):
        tipo=clasificar(i)
        contadores[tipo]+=1
        # ord > 127 significa que el carácter está fuera del ASCII estándar
        if tipo == "Raro" and ord(i) > 127:
            raros.append((pos, i)) 
    return contadores, raros

def extraer_dominio(texto_verificar):
     # Si tiene @ es un mail: el dominio es lo que va después de la @.
    if "@" in texto_verificar:
        textoemail=texto_verificar.split("@")[1]
        return textoemail
    # Si no, es una URL: se saca el protocolo y se corta en la primera "/"
    # para descartar la ruta (por ejemplo, /login).
    else:
        textoweb=texto_verificar.replace("https://", "").replace("http://","").split("/")[0]
        return textoweb
    
def nombre_unicode(caracter):
    # Devuelve el nombre oficial Unicode del carácter. Algunos no tienen
    # nombre (por ejemplo, un salto de línea) y en ese caso lanzan ValueError.
    try:
        return unicodedata.name(caracter)
    except ValueError:
        return "Sin Nombre"

def mostrar_analisis(dominio):
    # Analiza el dominio e imprime el veredicto. Se reutiliza desde
    # las opciones de mail y de URL del menú.
    contadores, raros= analizar(dominio)
    if len(raros)==0:
        print("Dominio limpio")
    else:
        print ("SOSPECHOSO")
        for pos, caracter in raros:
            # Solo se muestra "se parece a" si el carácter está en la tabla
            if caracter in parecidos:
                print("Posicion", pos , ":", caracter , nombre_unicode(caracter),"se parece a:", parecidos[caracter])
            else:
                print("Posicion", pos, ":", caracter, nombre_unicode(caracter))

# Menú principal: se repite hasta que el usuario elige la opción 3.
opcion=0
while opcion !=3:
    print("1) Analizar mail  2) Analizar URL  3) Salir")
    # Si el usuario escribe algo que no es un número, se avisa y se repite el menú
    try:
        opcion=int(input("Opcion: "))
    except ValueError:
        print("Escribi un numero: ")
        continue
    if opcion == 1:
        textomail_cli=input("Escribe el email a verificar :")
         # Un mail válido tiene exactamente una @
        if textomail_cli.count("@") !=1:
            print("Mail invalido")
        else:
            dominio=extraer_dominio(textomail_cli)
            print("Dominio: ", dominio)
            mostrar_analisis(dominio)
    elif opcion == 2:
        textoweb_cli=input("Escribe la direccion a verificar :")
        # Una URL con @ se rechaza (limitación conocida de la v1.0)
        if "@" in textoweb_cli:
            print("No es una direccion")
        else:
            dominio=extraer_dominio(textoweb_cli)
            print("Dominio: ", dominio)
            mostrar_analisis(dominio)
    elif opcion==3:
        print ("Muchas gracias por usar este programa.")
    else:
        print("No es un numero de la lista")
            
