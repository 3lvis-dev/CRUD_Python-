#CRUD - Create Read Update Delete.
#Manejo de Logging.

'''
Nota: pagina documentación: docs.python.org/3/howto/logging.html
'''
import psycopg2 as bd
import logging as log

log.basicConfig(level=log.DEBUG)

if __name__ == '__main__':
	log.debug('Mensaje a nivel debug')
	log.info('Mensaje a nivel info')
	log.warning('Mensaje a nivel warning')
	log.error('Mensaje a nivel error')
	log.critical('Mensaje a nivel critico')