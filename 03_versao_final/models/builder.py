from models.button import Botao

class BuilderCalc():
	def __init__(self, master, model):
		self.master = master
		self.model = model
		self.FONT_LARGE = ("Calibri", 12)

	def buildDigit(self, label:str):
		lambdaFun = lambda btn=label: self.model.get_variables(int(btn))
		return self.__templateBasico(label,lambdaFun)
		
	def buildOperator(self, label:str):
		lambdaFun = lambda btn=label: self.model.get_operation(btn)
		return self.__templateBasico(label,lambdaFun)
	
	def buildSpecial(self, label:str, callback:str, cor:str):
		if '{var_name}' in callback:
			#Um função lambda que demanda a inserção de uma variável
			callback = eval(callback.format(var_name=label), {'self':self})
		elif 'lambda' in callback:
			#nos casos em que a função callback é uma lambda
			callback = eval(callback, {'self':self})
		elif '.' in callback:
			#A função callback é um método, como "self.model.clear_all"
			parts = callback.split('.')
			ref = self
			for p in parts:
				ref = getattr(ref, p) if hasattr(ref, p) else ref
			callback = ref if callable(ref) else (lambda: None)
		else:
			try:
				callback = getattr(self.model, callback)
			except AttributeError:
				callback = lambda: None
		return Botao(label, self.FONT_LARGE, callback, cor, master=self.master)

	def buildAngle(self, label, methodName, cor):
		callback = lambda m=methodName: getattr(self.model, m)()
		return Botao(label, self.FONT_LARGE, callback, cor, master=self.master)

	def buildCustom(self, label, callback, cor):
		if hasattr(self.model, callback):
			callback = getattr(self.model, callback)
		else:
			try:
				callback = eval(callback, {'self': self})
			except Exception:
				callback = lambda: None
		return Botao(label, self.FONT_LARGE, callback, cor, master=self.master)

	def __templateBasico(self,label,lambdaFun):
		return Botao(label, self.FONT_LARGE,lambdaFun,"black", master=self.master)