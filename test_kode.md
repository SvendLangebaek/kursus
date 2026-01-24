# Opgave: Du har et eksisterende program.<br/> Dette program er struktureret i klasser og mapper<br/>Vi skal lave en automatisk test af programmet
<br/><br/>

## Delopgave 1
Opret en mappe med navnet "tests", under denne mappe opret en python fil hvor navnet starter med "test_" og slutter med navnet på den fil der skal testes.<br/>Det er en god ide at lade strukturen i tests være et spejl af programmets struktur

## Delopgave 2
Lav en test klasse. Importer TestCase fra unittest og nedarv den i din testklasse

## Hints 2
Importer med:

	from unittest import TestCase

en klasse nedarver fra en anden klasse ved at angive navnet i ()<br/>
F.eks.


	class TestDemo(TestCase):

## Delopgave 3
Lav en metode i test klassen der tester en metode fra en anden klasse<br/>

## Hint 3
Husk at en metode laves med

	def metodenavn(self):
		print()

Importer den klasse der skal testes med

	import mappe.fil.klasse

eller

	from mappe.fil import klasse

## Delopgave 4
Udfør testen

## Hint 4
Udfør test med

	python -m unittest mappenavn.filnavn.klassenavn.metodenavn

Bemærk at at stien kan forkortes til at inkludere alle under den
dvs. for vores mappe med navnet tests kan alle tests udføres med

	python -m unittest tests.filnavn

Ønsker man at udføre alle filer under en mappe kan det gøres med

	python -m unittest discover mappenavn
