## https://github.com/SvendLangebaek/kursus/blob/main/basis.md
## Grundlæggende variable typer

heltal<br/>
x = 10

kommatal<br/>
x = 1.3

tekst - både " og ' kan bruges til definition<br/>
x = "tekst"

liste - en liste af objekter, tilgå hvert element med x[index] hvor index er nummer på det element du gerne vil arbejde med<br/>
x = [1, 2, 3]<br/>
en liste har metoden append der bruges til at tilføje nye elementer<br/>

tuple - en liste der ikke kan ændres efter den er defineret<br/>
x = (1, 2, 3)<br/>

set - set er en uniq liste af elementer, vær opmærksom på at ikke alle elementer kan bruges i et sæt. Fokuser evt. mere på andre variable typer<br/>
x = {1, 2, 3}<br/>

dictionary - en dictionary er en "ordbogs" struktur<br/>
x = {"a": 1, "b": 2}<br/>
tænk på det som en liste hvor man i stedet tilgår elementerne med et navn f.eks. x["a"] = 3

x = True<br/>
eller<br/>
x = False<br/>


## indbyggede metoder <br/>
print()
udskriver tekst, brug evt. formateret tekst med f.eks. f'a= {}'

len()
giver længden af visse typer, ofte brugt sammen med lister, tupler etc.

help()
viser hjælpetekst om den type, det er den samme tekst der kommer frem ved at holde musen over

input("tekst: ")<br/>
brug denne til at opfange en indtastning, teksten <br/> 

type()<br/>
Er du i tvivl om hvilken type din variabel er, brug denne metode<br/>

range()<br/>
Denne metode giver en range, bruges ofte sammen med for<br/>

## konverter mellem typer med følgende
x = str(123)<br/>
x = int('10')<br/>
x = float('10.5')<br/>
x = list((1, 2, 3))<br/>
x = dict(a=1, b=2)<br/>

## kontrol strukturer
if<br/>
afgør om det der er under if udføres<br/>

else<br/>
udføres hvis det der er i if statement ikke er sand<br/>

for x in y<br/>
udføre en løkke, i hver gennemløb sættes x til den næste værdi i y. for bruges ofte sammen med range() eller lister

while<br/>
en løkke der kører så længe udtrykket efter den er sand<br/>

break<br/>
brug denne til at stoppe en løkke før den ellers ville stoppe, bruges ofte i forbindelse med lange lister<br/>

continue<br/>
hopper til toppen af løkken, vent evt. med denne<br/>
