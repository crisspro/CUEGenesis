import os
import pickle
import requests
import webbrowser

from modelo.marca import *
from modelo.tiempo import Tiempo

class Controlador():
	def __init__(self):
		self.data  = None
		self.ruta_proyecto = 'temp.proyecto.cgp'


	def verificarNuevaVersion(self):
		try:
			link= 'https://api.github.com/repos/crisspro/cuegenesis/releases/latest'
			coneccion= requests.get(link, timeout= 5)
		except(requests.ConectionError, requests.Timeout):
			print('No hay conección')
		else:
			print('Hay conección')
			v= coneccion.json() ['tag_name']
			if v != version_app:
				wx.adv.Sound.PlaySound(os.path.join('vista', 'sounds', 'nueva_version.wav'))
				resp= wx.MessageBox('Hay disponible una nueva versión de ' + nombre_app + '(' + v + ')' + '. ¿Quieres descargarla ahora?', caption= 'Aviso', style= wx.YES_NO)
				if resp == wx.YES:
					dw= coneccion.json() ['assets']
					for i in dw:
						dw= i['browser_download_url']
					webbrowser.open(dw)
					self.Close()

	def crearMarca(self, *args, **kwargs):
		marca = Marca(*args, **kwargs)
		self.data.agregarMarca(marca)
		self.save()
		return marca

	def getMarcas(self):
		return self.data.getMarcas()
	
	def load(self):
		""" carga la información del modelo. """
		try:
			f = open(self.ruta_proyecto , "rb")
			self.data = pickle.load(f)
			f.close()
		except FileNotFoundError:
			self.data = Data()
	
	def save(self):
		""" guarda la información del modelo """
		f = open(self.ruta_proyecto , 'wb')
		pickle.dump(self.data, f)
		f.close()

	def limpiar_temporal(self):
		if os.path.exists('temp.proyecto.cgp'):
			os.remove('temp.proyecto.cgp')

