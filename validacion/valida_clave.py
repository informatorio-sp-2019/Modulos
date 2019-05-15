"""
MÓDULO VALIDA CLAVE
•	La contraseña debe contener un mínimo de 8 caracteres.
•	Una contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico.
•	La contraseña no puede contener espacios en blanco.
•	Contraseña válida, retorna True.
•	Contraseña no válida, retorna el mensaje "La contraseña elegida no es segura".
"""


#Función para validar caracter no alfanumérico

def valida_caracter_no_alfanum(clave):
    lRetorno = False
    for c in clave:
        if not c.isalnum():
            lRetorno = True
            break

    return lRetorno   