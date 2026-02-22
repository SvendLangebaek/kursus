from FoedevareParameter import FoedevareParameter


class Foedevare:
	def __init__(self, foedevare: dict):
		self.ID = foedevare['FoodID']
		self.Navn = foedevare['FødevareNavn']
		self.Name = foedevare['FoodName']
		self._parameters = {}
		self.tilfoej_parameter(foedevare)

	def tilfoej_parameter(self, foedevare):
		self._parameters[foedevare['FødevareNavn']] = FoedevareParameter.fra_dict(foedevare)

	def __repr__(self):
		indre = ''
		for ID in self._parameters:
			indre += str(self._parameters[ID])
		return f'\n{self.Navn} / {self.Name}\n{indre}'
