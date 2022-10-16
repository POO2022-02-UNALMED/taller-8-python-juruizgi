from deportista import Deportista
from persona import Persona

class Futbolista(Deportista, Persona):
	_listaFutbolistas = []
	def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
		super().__init__("Futbol", añosPracticando,nombre, edad, altura, sexo)
		self._golesMarcados = golesMarcados
		self._tarjetasRojas = tarjetasRojas
		self._piernaHabil = piernaHabil
		self._listaFutbolistas.append(self)


	def getGolesMarcados(self):
		return self._golesMarcados

	def setGolesMarcados(self,g):
		self._golesMarcados = g

	def getTarjetasRojas(self):
		return self._tarjetasRojas

	def setTarjetasRojas(self,t):
		self._tarjetasRojas = t

	def getPiernaHabil(self):
		return self._piernaHabil

	def setPiernaHabil(self,p):
		self._piernaHabil = p

	@classmethod
	def getListaFutbolistas(cls):
		return cls._listaFutbolistas

	@classmethod	
	def setListaFutbolistas(cls, l):
		cls._listaFutbolistas = l

	def __str__(self):
		return f"Mi nombre es {self.getNombre()} soy profesional en el deporte {self.getDeporte()} Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte"


if __name__ == "__main__":
	
	futbolista = Futbolista("Juan Pablo", 30, "1,80", "M", 12, 400, 1, "Derecha")
	print(futbolista.__str__() == "Mi nombre es Juan Pablo soy profesional en el deporte Futbol Tengo 30 años de edad y llevo 12 años en el deporte")

	deportista =  Persona("guaracha", "fercho","m","lolp")
	print(deportista.getAltura())
