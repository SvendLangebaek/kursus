import data
import vis


query = input('Hvad søger du ? ')
data_format = input('Hvordan vil du have resultatet (txt eller json) ? ')
output_type = input('Gem eller Vis resultatet ? ')

tabel = data.hent_tabel()
liste = data.tabel_til_liste(tabel)
liste = data.filtrer_liste_paa_parameter_id(liste, 356)
liste = data.filtrer_liste_paa_navn(liste, query)

if data_format == 'txt':
	tekst = data.liste_til_eget_format(liste)
elif data_format == 'json':
	tekst = data.liste_til_json(liste)
else:
	raise Exception(f'Formatet "{data_format}" er ukendt, vælg i stedet enten txt eller json')

if output_type == 'vis':
	vis.vis_tekst(tekst)
elif output_type == 'gem':
	if data_format == 'txt':
		vis.gem_som_fil(tekst, 'txt')
	if data_format == 'json':
		vis.gem_som_fil(tekst, 'json')
