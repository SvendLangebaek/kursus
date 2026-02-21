from polars import read_excel
import json
from typing import List


def hent_tabel():
	return read_excel("Frida.xlsx", sheet_id=3)

def tabel_til_liste(tabel) -> List[dict]:
	"""
	laver en tabel om til en liste
	:param tabel: den tabel der skal laves om
	:return: en liste af dict
	"""
	result = []
	for row in tabel.iter_rows(named=True):
		result.append(row)
	return result

def filtrer_liste_paa_navn(liste: List[dict], query: str) -> List[dict]:
	result = []
	for row in liste:
		if query in row['FødevareNavn']:
			result.append(row)
	return result

def filtrer_liste_paa_parameter_id(liste: List[dict], parameter_id: int) -> List[dict]:
	result = []
	for row in liste:
		if parameter_id == row['ParameterID']:
			result.append(row)
	return result

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
