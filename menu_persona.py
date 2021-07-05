#Capa de Datos.
#Menu Usuario.

'''
Nota: 
'''

from clase_dao import PersonaDAO
from clase_persona import Persona
from logger_base import log

opcion = None
while opcion != 5:
	print('Opciones:')
	print('1. Listar usuarios')
	print('2. Agregar usuario')
	print('3. Modificar usuario')
	print('4. Eliminar usuario')
	print('5. Salir')
	opcion = int(input('Escribe tu opcion (1-5):'))
	if opcion == 1:
		personas = PersonaDAO.seleccionar()
		for persona in personas:
			log.info(persona)
	elif opcion == 2:
		username_var = input('Escribe el username: ')
		nombre_var = input('Escribe el nombre: ')
		apellido_var = input('Escribe el apellido: ')
		email_var = input('Escribe el email: ')
		password_var = input('Escribe el password: ')
		telefono_var = input('Escribe el teléfono: ')
		persona = Persona(username=username_var, nombre=nombre_var,
			apellido=apellido_var, email=email_var, password=password_var,
			telefono=telefono_var)
		personas_insertados = PersonaDAO.insertar(persona)
		log.info(f'Personas insertados: {personas_insertados}')
	elif opcion == 3:
		id_persona_var =int(input('Escribe el id usuario a modificar: '))
		username_var = input('Escribe el username: ')
		nombre_var = input('Escribe el nombre: ')
		apellido_var = input('Escribe el apellido: ')
		email_var = input('Escribe el email: ')
		password_var = input('Escribe el password: ')
		telefono_var = input('Escribe el teléfono: ')
		persona = Persona(id_persona_var, username_var, nombre_var, 
			apellido_var, email_var, password_var, telefono_var)
		personas_actualizados = PersonaDAO.actualizar(persona)
		log.info(f'Personas actualizados: {personas_actualizados}')
	elif opcion == 4:
		id_persona_var = int(input('Escribe el id a eliminar: '))
		persona = Persona(id_persona=id_persona_var)
		personas_eliminados = PersonaDAO.eliminar(persona)
		log.info(f'Persona eliminada: {personas_eliminados}')
else:
	log.info('Salimos de la aplicación') 	
	

#if __name__ == '__main__':