class FoedevareParameter:
	def __init__(self, navn, name, res_val, res_min, res_max):
		self.navn = navn
		self.name = name
		self.res_val = res_val
		self.res_min = res_min
		self.res_max = res_max

	@classmethod
	def fra_dict(cls, foedevare: dict):
		return FoedevareParameter(
			navn=foedevare['ParameterNavn'],
			name=foedevare['ParameterName'],
			res_val=foedevare['ResVal'],
			res_min=foedevare['Min'],
			res_max=foedevare['Max'],
		)

	def __repr__(self):
		return f'\n\t\t{self.navn} | {self.name} = {self.res_val}'
