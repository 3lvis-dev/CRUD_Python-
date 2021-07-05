#Capa de Datos.
#Clase Persona.

'''
Nota: 
'''
#import psycopg2 as bd
from logger_base import log

class Persona():
	"""docstring for Persona"""
	def __init__(self, id_persona=None, 
				username=None, nombre=None, apellido=None, 
				email=None, password=None, telefono=None
		):
		self._id_persona = id_persona
		self._username = username
		self._nombre = nombre
		self._apellido = apellido
		self._email = email
		self._password = password
		self._telefono = telefono

	def __str__(self):
		return f''' 
			ID Persona: {self._id_persona}
			Username: Nombre: Apellido: 
			{self._username} {self._nombre} {self._apellido}
			Email: Password: Telefono: 
			{self._email} {self._password} {self._telefono}
		'''	
		
	@property #Metodo Get ID Persona
	def id_persona(self):
		return self._id_persona

	@id_persona.setter #Metodo Set ID Persona
	def id_persona(self, id_persona):
		self._id_persona = id_persona

	@property #Metodo Get Username
	def username(self):
		return self._username

	@username.setter #Metodo Set Username
	def username(self, username):
		self._username = username

	@property #Metodo Get Nombre
	def nombre(self):
		return self._nombre

	@nombre.setter #Metodo Set Nombre
	def nombre(self, nombre):
		self._nombre = nombre

	@property #Metodo Get Apellido
	def apellido(self):
		return self._apellido

	@apellido.setter #Metodo Set Apellido
	def apellido(self, apellido):
		self._apellido = apellido

	@property #Metodo Get Email
	def email(self):
		return self._email

	@email.setter #Metodo Set Email
	def email(self, email):
		self._email = email

	@property #Metodo Get Password
	def password(self):
		return self._password

	@password.setter #Metodo Set Password
	def password(self, password):
		self._password = password

	@property #Metodo Get telefono
	def telefono(self):
		return self._telefono

	@telefono.setter #Metodo Set Telefono
	def telefono(self, telefono):
		self._telefono = telefono
	
	
#if __name__ == '__main__':
	#persona1 = Persona(1, 'Nikolas', 'Tesla', 'ntesla@mail.com')	
	#log.debug(persona1)
	
	#Simulando un insert
	#persona2 = Persona(nombre='Nikolas',apellido='Tesla',email='ntesla@mail.com')
	#log.debug(persona2)

	#Simulación delete
	#persona3 = Persona(id_persona=1)
	#log.debug(persona3)
