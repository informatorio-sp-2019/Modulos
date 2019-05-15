"""
MÓDULO VALIDA CLAVE
•	La contraseña debe contener un mínimo de 8 caracteres.
•	Una contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico.
•	La contraseña no puede contener espacios en blanco.
•	Contraseña válida, retorna True.
•	Contraseña no válida, retorna el mensaje "La contraseña elegida no es segura".
"""

def valida_long_min(clave):
	"""
	+ recibe un str
	+ evalua longitud mínima de 8
	+ retorna un valor booleano
	"""
	if len(clave) < 8:
		lRetorno = False
	else:
		lRetorno = True

	return lRetorno

def valida_minuscula(clave):
	return clave.islower()

def valida_mayuscula(clave):
	return clave.isupper()

#Función para validar caracter no alfanumérico

def valida_caracter_no_alfanum(clave):
    lRetorno = False
    for c in clave:
        if not c.isalnum():
            lRetorno = True
            break

    return lRetorno   

def valida_espacios(clave):
	return ' ' in clave


