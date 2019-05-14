"""
•	El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12.
•	El nombre de usuario debe ser alfanumérico.

"""

def valida_long_min(usuario):
	if len(usuario) < 6:
		lRetorno = False
	else:
		lRetorno = True	

	return lRetorno

def valida_long_max(usuario):
	if len(usuario) > 12:
		lRetorno = False
	else:
		lRetorno = True

	return lRetorno
