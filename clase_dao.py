#Capa de Datos.
#Clase Persona DAO.

'''
Nota: 
'''
#import psycopg2 as bd
from logger_base import log
from conexion import Conexion
from clase_persona import Persona
from cursor_del_pool import CursorDelPool
#import sys


class PersonaDAO():
	"""DAO (Data Access Object)"""
	_SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
	_INSERTAR = 'INSERT INTO persona(username,nombre,apellido,email,password,telefono) VALUES(%s,%s,%s,%s,%s,%s)' 
	_ACTUALIZAR = 'UPDATE persona SET username=%s,nombre=%s,apellido=%s,email=%s,password=%s,telefono=%s WHERE id_persona=%s'
	_ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

	@classmethod
	def seleccionar(cls):
		with CursorDelPool() as cursor:
			cursor.execute(cls._SELECCIONAR)
			registros = cursor.fetchall()
			personas = []
			for registro in registros:
				persona = Persona(registro[0],
					registro[1],registro[2],registro[3],
					registro[4],registro[5],registro[6]
					)
				personas.append(persona)
			return personas

	@classmethod
	def insertar(cls, persona):
		with CursorDelPool() as cursor:
			valores = (persona.username, persona.nombre, persona.apellido, 
				persona.email, persona.password, persona.telefono)
			cursor.execute(cls._INSERTAR, valores)
			log.debug(f'Persona insertada: {persona}')
			return cursor.rowcount

	@classmethod
	def actualizar(cls, persona):
		with CursorDelPool() as cursor:
			valores = (persona.username, persona.nombre, persona.apellido, 
				persona.email, persona.password, persona.telefono, 
				persona.id_persona)
			cursor.execute(cls._ACTUALIZAR, valores)
			log.debug(f'Persona actualizada: {persona}')
			return cursor.rowcount

	@classmethod
	def eliminar(cls, persona):
		with CursorDelPool() as cursor:
			valores = (persona.id_persona,)
			cursor.execute(cls._ELIMINAR, valores)
			log.debug(f'Persona eliminada: {persona}')
			return cursor.rowcount


#PRUEBAS DE LA CLASE y OBJETOS
#if __name__ == '__main__':

	#Eliminar Objetos
	#persona1 = Persona(id_persona=5)
	#personas_eliminadas = PersonaDAO.eliminar(persona1)
	#log.debug(f'Personas eliminadas: {personas_eliminadas}')

	#Actualizar Objetos
	#persona1 = Persona(5, 'scooper', 'Sheldon', 'Cooper', 'scooper@mail.com', 'scooper123', '1234567')
	#personas_actualizadas = PersonaDAO.actualizar(persona1)
	#log.debug(f'Personas actualizadas: {personas_actualizadas}')

	#Insertar Objetos
	#persona1 = Persona(username='scooper',nombre='Sheldon',apellido='Cooper',email='scooper@mail.com',password='scooper123')
	#personas_insertadas = PersonaDAO.insertar(persona1)
	#log.debug(f'Personas insertadas: {personas_insertadas}')

	#Seleccionar Objetos
	#personas = PersonaDAO.seleccionar()
	#for persona in personas:
	#	log.debug(persona)

	