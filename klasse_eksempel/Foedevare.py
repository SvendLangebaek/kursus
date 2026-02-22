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

	def to_dict(self):
		return {
			'ID': self.ID,
			'Navn': self.Navn,
			'Name': self.Name,
			'Parameters': self._parameters_to_dict(),
		}

	def _parameters_to_dict(self):
		parameters = []
		for parameter_key in self._parameters:
			parameters.append(self._parameters[parameter_key].to_dict())
		return parameters

	def __repr__(self):
		indre = ''
		for ID in self._parameters:
			indre += str(self._parameters[ID])
		return f'\n{self.Navn} / {self.Name}\n{indre}'
