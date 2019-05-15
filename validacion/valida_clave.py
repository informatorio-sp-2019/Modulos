"""
MÓDULO VALIDA CLAVE
•	La contraseña debe contener un mínimo de 8 caracteres.
•	Una contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico.
•	La contraseña no puede contener espacios en blanco.
•	Contraseña válida, retorna True.
•	Contraseña no válida, retorna el mensaje "La contraseña elegida no es segura".
"""


"""" La contraseña debe contener valores numericos """
def valida_caracter_numerico(clave):
	lRetorno = False
	for c in clave:
		if c.isdigit():
			lRetorno = True
			break

	return lRetorno
