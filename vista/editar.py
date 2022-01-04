import wx

from controlador import Controlador

class Editar(wx.Dialog):
	def __init__(self, parent, title):
		super().__init__(parent, title= title)
		self.Center()
#		self.controlador = Controlador()

		panel1= wx.Panel(self)
		self.l_titulo = wx.StaticText(panel1, -1, 'Título:')
		self.in_titulo= wx.TextCtrl(panel1)
		self.in_titulo.SetFocus()
		self.Bind(wx.EVT_TEXT, self.evento_texto, self.in_titulo)
		self.l_autor= wx.StaticText(panel1, -1, 'Autor:')
		self.in_autor= wx.TextCtrl(panel1, -1)
		self.Bind (wx.EVT_TEXT, self.evento_texto, self.in_autor)		
		self.l_horas= wx.StaticText(panel1, -1, 'Horas')
		self.in_horas= wx.SpinCtrl(panel1)
		self.in_horas.SetRange(0,24)
		self.l_minutos= wx.StaticText(panel1, -1, 'Minutos')
		self.in_minutos= wx.SpinCtrl(panel1)
		self.in_minutos.SetRange(0,59)
		self.l_segundos= wx.StaticText(panel1, -1, 'Segundos')
		self.in_segundos= wx.SpinCtrl(panel1)
		self.in_segundos.SetRange(0,59)
		self.l_marcos= wx.StaticText(panel1, -1, 'Marcos')
		self.in_marcos= wx.SpinCtrl(panel1)
		self.in_marcos.SetRange(0,74)
		self.bt_reproducir= wx.Button(panel1, -1, '&Reproducir')
		#self.Bind(wx.EVT_BUTTON, Programa.reproducir_pausar, self.bt_reproducir)
		self.bt_aceptar= wx.Button(panel1, wx.ID_OK, '&Aceptar')
		self.bt_aceptar.Enable(False)
		self.bt_cancelar= wx.Button(panel1, wx.ID_CANCEL, '&Cancelar')




	def getAutor(self):
		return self.in_autor.GetValue()
	
	def getTitulo(self):
		return self.in_titulo.GetValue()
	
	def getTiempoInicio(self):
		return (self.in_horas.GetValue(), self.in_minutos.GetValue(), self.in_segundos.GetValue(), self.in_marcos.GetValue())	

	def alertar(self):
		if self.in_autor.GetValue() == '':
			wx.MessageBox('Debes ingresar un autor.', 'Alerta.')
		elif self.in_titulo.GetValue() == '':
			wx.MessageBox('Debe ingresar un título.', 'Alerta.')

	def getTiempo(self, milesimas):
		controlador.temporizar(milesimas)
		tiempo = controlador.cargar_tiempo()
		self.in_marcos.SetValue(tiempo[3]) 
		self.in_segundos.SetValue(tiempo[2])
		self.in_minutos.SetValue(tiempo[1])
		self.in_horas.SetValue(tiempo[0])



	def evento_texto (self, event):
		self.evalua_llenado()

	#evalúa el correcto llenado del formulario
	def evalua_llenado(self):
		if self.in_autor.GetValue() != '' and self.in_titulo.GetValue() != '':
			self.bt_aceptar.Enable(True)
		else:
			self.bt_aceptar.Enable(False)


controlador =Controlador()