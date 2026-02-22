from polars import read_excel
import json
from Foedevare import Foedevare


def hent_tabel():
	return read_excel("Frida.xlsx", sheet_id=3)

def tabel_til_dict(tabel) -> dict:
	result = {}
	for row in tabel.iter_rows(named=True):
		food_id = row['FødevareNavn']
		if result.get(food_id):
			result[food_id].tilfoej_parameter(row)
		else:
			result[food_id] = Foedevare(row)
	return result

def filtrer_dict_paa_navn(food_dict: dict, query: str):
	doomed_keys = []
	for key in food_dict.keys():
		if query not in key:
			doomed_keys.append(key)
	for key in doomed_keys:
		del food_dict[key]

def dict_til_json(liste):
	class JsonEncoder(json.JSONEncoder):
		def default(self, obj):
			return obj.to_dict()

	return json.dumps(liste, cls=JsonEncoder)

def dict_til_eget_format(food_dict: dict):
	foedevare_liste = []
	for key in food_dict:
		foedevare_liste.append(str(food_dict[key]))
	print(foedevare_liste)
	return '\n'.join(foedevare_liste)
