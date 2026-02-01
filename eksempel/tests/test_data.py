from unittest import TestCase
import data


class test_data(TestCase):
	def test_filtrer_liste_paa_navn_filtrere_en_liste(self):
		test_liste = [
			{'FødevareNavn': 'abcde'},
			{'FødevareNavn': 'cdefgh'},
		]

		faktisk_liste = data.filtrer_liste_paa_navn(test_liste, 'def')

		forventet_liste = [
			{'FødevareNavn': 'cdefgh'},
		]

		self.assertEqual(forventet_liste, faktisk_liste)
