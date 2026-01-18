#Opgave:
#Lav et command line opslagsværk, der kan give information om mad
<br/><br/><br/>

## Delopgave 1
programmet skal kunne tage et input<br/>
prøv i første omgang bare at skrive det ud


## Hints 1
Hent metoder ind via import <br/>
python har en del forskellige metoder i forskellige module<br/>
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
Open indstillinger med ctrl-alt-s og se under interpreter.<br/>
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
Den simpleste vej er at bruge <code> .iter_rows(named=True) </code><br/>
på den frame man får tilbage<br/>
På den måde ser vi data som en dict (en dict I python er en dictionary) i stedet for en frame
<br/><br/>
<pre><code>for row in **frame**.iter_rows(named=True):
&emsp;print(row)<br/>&emsp;break</code>
</pre><br/>
<br/>bemærk at <code>break</code> kommandoen afbryder iterationen efter første gennemløb
<br/>

## Delopgave 5
Som input skal man kunne vælge at gemme output som en json fil
Importer det indbyggede modul **json**<br/>
## Hints 5
Brug <code>json.dumps(**name**)</code> til at omdanne fra en dict til json format<br/>
Herefter kan filen skrives med<pre><code>with open('/path/to/file.json', 'w') as **file**:
&emsp;file.write(**json_formatted_string**)</code></pre>

## Delopgave 6
Flyt en del af programmet over i an anden fil tænk over den struktur du gerne vil have i dit program

## Hints 6
Python filer kan importeres på samme måde som installerede pakker<br/>
Bemærk at stien er relativ og adskilles med "." og ikke med "/"
I særlige tilfælde som f.eks. plugins bruger man relative stier, de starter med .


