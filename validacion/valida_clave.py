"""
MÓDULO VALIDA CLAVE
•	La contraseña debe contener un mínimo de 8 caracteres.
•	Una contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico.
•	La contraseña no puede contener espacios en blanco.
•	Contraseña válida, retorna True.
•	Contraseña no válida, retorna el mensaje "La contraseña elegida no es segura".
"""

def valida_espacios(clave):
	return ' ' in clave