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


def liste_til_json(liste):
	return json.dumps(liste)

def liste_til_eget_format(liste: List[dict]):
	indre_skabelon = '''
	{dansk:<40} {engelsk:<40}
	'''
	ydre_skabelon = '''
	-------------------------------------------------------------
	{indre}
	-------------------------------------------------------------
	'''
	indre = ""
	for row in liste:
		indre += indre_skabelon.format(dansk=row['FødevareNavn'], engelsk=row['FoodName'])
	total = ydre_skabelon.format(indre=indre)
	return total
