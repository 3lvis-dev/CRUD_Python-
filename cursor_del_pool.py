#CRUD - Create Read Update Delete.
#Cursor del pool.

'''
Nota: 
'''
#from psycopg2 import pool 
from logger_base import log
from conexion import Conexion
#import sys


class CursorDelPool():
	"""docstring for CursorDelPool"""
	def __init__(self):
		self._conexion = None
		self._cursor = None

	def __enter__(self):
	 	log.debug('Inicio del metodo with enter')
	 	self._conexion = Conexion.obtenerConexion()
	 	self._cursor = self._conexion.cursor()
	 	return self._cursor

	def __exit__(self, tipo_exception, valor_exception, detalle_exception):
		log.debug('Se ejecuta método exit')
		if valor_exception:
			self._conexion.rollback()
			log.error(f'Ocurrió una exception, se hace rollback {valor_exception}')
		else:
			self._conexion.commit()
			log.debug('Commit de la transacción')
		self._cursor.close()
		Conexion.liberarConexion(self._conexion)

		

#Prueba para comprobar que el Cursor del pool funciona correctamente.	
if __name__ == '__main__':
#Prueba de select a la base de datos
	with CursorDelPool() as cursor:
		log.debug('Dentro del bloque with')
		cursor.execute('SELECT * FROM persona')
		registros = cursor.fetchall()
		registro = []
		for registro in registros:
			log.debug(registro)

	