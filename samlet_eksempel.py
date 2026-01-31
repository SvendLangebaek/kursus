from polars import read_excel
import json

# spørger brugeren hvad der søges efter
query = input('Hvad søger du ? ')
data_format = input('Hvordan vil du have resultatet (txt eller json) ? ')
output_type = input('Gem eller Vis resultatet ? ')

# hent tabellen fra excel ark
tabel = read_excel("Frida.xlsx", sheet_id=3)

# flyt tabellen over i en liste
liste = []
for row in tabel.iter_rows(named=True):
	liste.append(row)

# find kun de fødevare der blev spurgt efter
ny_liste = []
for row in liste:
	if query in row['FødevareNavn']:
		ny_liste.append(row)
liste = ny_liste

# filtrer på en enkelt parameter id
ny_liste = []
for row in liste:
	if 356 == row['ParameterID']:
		ny_liste.append(row)
liste = ny_liste

# omdanner listen til tekst
if data_format == 'txt':
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
	tekst = ydre_skabelon.format(indre=indre)
elif data_format == 'json':
	tekst = json.dumps(liste)
else:
	raise Exception(f'Formatet "{data_format}" er ukendt, vælg i stedet enten txt eller json')

# viser eller gemmer teksten
if output_type == 'vis':
	print(tekst)
elif output_type == 'gem':
	if data_format == 'txt':
		with open('output.txt', 'w') as file:
			file.write(tekst)
	if data_format == 'json':
		with open('output.json', 'w') as file:
			file.write(tekst)
