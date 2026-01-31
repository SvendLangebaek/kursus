def vis_liste(liste):
	for row in liste:
		print(row)

def vis_tekst(tekst):
	print(tekst)

def vis_liste_dansk_engelsk(liste):
	for row in liste:
		dansk = row['FødevareNavn']
		engelsk = row['FoodName']
		print(f'{dansk:<15} - {engelsk:<15}')

def gem_som_fil(tekst, fil_type='json'):
	with open(f'output.{fil_type}', 'w') as file:
		file.write(tekst)
