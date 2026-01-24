## https://github.com/SvendLangebaek/kursus/blob/main/python_opgave_mad.md
# Opgave:
# Lav et command line opslagsværk, der kan give information om mad
<br/><br/><br/>

## Delopgave 1
programmet skal kunne tage et input<br/>
prøv i første omgang bare at skrive det ud


## Hints 1
Hent metoder ind via import <br/>
python har en del forskellige metoder i forskellige moduler<br/>
Et modul hentes med kommandoen <br/>
<code> import </code><br/> f.eks.<br/>
<code> from sys import argv </code><br/>
argv er en liste<br/>
OBS argv giver ikke mening I notebook<br/>
eller brug den indbyggede metode<br/><code>input("tekst: ")</code>


## Delopgave 2
på baggrund af input skal der vises noget data<br/>
data kan hentes på<br/>https://frida.fooddata.dk/data? <br/>
du downloader der en zipfil med et excel ark, dette udpakkes i projektet

## Delopgave 3
For at vi kan arbejde med data skal de hentes ind i python<br/>
her skal vi bruge nogle pakker fra pypi
Det er en god ide at checke om python fortolkeren er sat rigtigt op.<br/>
## Hints 3
Open indstillinger med ctrl-alt-s og se under python->interpreter.<br/>
Der kan der også installeres pakker<br/>
pakkerne polars og fastexcel kan bruges her<br/>
Ønsker man en manuel installation kan man i uv installere en pakke med<br/>
<code>uv add **pakkenavn**</code>
med pip installeres en pakke med<br/>
<code>pip install **pakkenavn**</code>

## Delopgave 4
Programmet tager navnet på en madvarer og giver en eller flere informationer om den.<br/>
Eksperimenter med hvad programmet skal tage ind og give ud
## Hints 4
Importer de pakker vi lige har installeret
<br/>
<code>from polars import read_excel, col</code>
<br/><code>read_excel(**navn**, sheet_id=**id**) </code><br/><br/>
Den simpleste måde at tilgå data er at bruge <code> .iter_rows(named=True) </code><br/>
på det objekt man får tilbage fra metoden read_excel<br/>
På den måde ser vi data som en dict (en dict I python er en dictionary)
<br/><br/>
<pre><code>for row in object_name.iter_rows(named=True):
&emsp;print(row)<br/>&emsp;break</code>
</pre><br/>
<br/>bemærk at <code>break</code> kommandoen afbryder iterationen efter første gennemløb
<br/>

## Delopgave 5
Som input skal man kunne vælge at gemme output som en json fil
Importer det indbyggede modul **json**<br/>
## Hints 5
Brug <code>json.dumps(**name**)</code> til at omdanne fra en dict til json format<br/>
Herefter kan filen skrives med

	with open('/path/to/file.json', 'w') as file:
		file.write(json_formatted_string)

Har du behov for at slette et element for at kunne konvertere, kan det gøres med

	del dict_variable['navn']

## Delopgave 6
Flyt en del af programmet over i an anden fil tænk over den struktur du gerne vil have i dit program

## Hints 6
Python filer kan importeres på samme måde som installerede pakker<br/>
Bemærk at stien starter i samme mappe som det python program du starter og adskilles med "." og ikke med "/"
I særlige tilfælde som f.eks. plugins bruger man relative stier, de starter med .

## Delopgave 7
Organiser din kode i en eller flere klasser

## Hints 7
Typisk har en fil kun en klasse, dette er ikke et krav, og afhænger af den struktur du gerne vil bruge<br/>
En klass oprettes med<br/>
<pre><code>class class_name:<br/>&emsp;def __init__(self):
&emsp;&emsp;print('initialize')
</code></pre><br/>
Klassen kan bruges på samme måde som de indbyggede klasser, et object laves med<br/>
<code>var_name = class_name()</code><br/>
variablen <code>self</code> referere til det object der er blevet lavet<br/>
Efterfølgende metoder der oprettes i klassen har alle argumentet self, det kan man bruge til at arbejde med metoder og variable<br/>

## Delopgave 8
Definer dit eget output format

## Hints 8
Et format kan defineres som en string hvor de ting der skal byttes ud markeres med {navn}
f.eks.

	template = 'en ting {navn1} - {navn2}'
	filled_template = template.format(navn1=1, navn2=2)

En string kan strække sig over flere linjer ved at bruge '''
F.eks.

	template = '''
		tekst der skal vises
	'''

Escape { med dobbelt {{
