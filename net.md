## Netværk
### Netværk er et komplekst emne, der er mange muligheder, vi starter med de mest simple
### Start en simpel server med python -m http.server
### Test serveren med en browser http://127.0.0.1:8000/ find in json fil at teste med
### I en jupyter notebook importer metoden get fra det indbyggede modul requests
### Prøv at kalde get metoden med en test url, hvad er resultatet
### Find den kode du fik tilbage på denne liste over status koder https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
### Undersøg Response objektet enten med mus over eller med den indbyggede metode help
### Hent en json fil, konverter den til json
### Vi bemærker at pythons indbyggede http.server ikke understøtter alle de metoder vi forventer af et moderne api, se https://restfulapi.net/http-methods/ for en liste af de metoder sådan et api forventes at have
### Stop serveren
## - Lav en bedre server
### Indstaller pakken "fastapi[standard]" hvis du bruger uv så er det kommandoen uv add "fastapi[standard]" med pip er det pin install "fastapi[standard]". Eller brug pycharms package install under settings (ctrl-alt-s)
### Opret en python fil med kode fastapi's standard eksempel på https://pypi.org/project/fastapi/ (Undgå indtil videre async)
### Start serveren med fastapi dev <filnavn>
### Test igen i jupyter notebook
### Bemærk at fastapi automatisk laver dokumentation se den på http://127.0.0.1:8000/docs Denne dokumentation kan også bruges til test
### - Eksemplet fra fastapi lægger op til at vi gemmer og henter nogle items</br> men det gør de ikke... Lad os fortsætte eksemplet så root kald angiver hvor mange items der er gemt, read_item henter en item, og vi tilføjer en create_item metode til at oprette et item
### Importer BaseModel fra pydantic, dette kan bruges til at definere et item. Det gøres ved at lave en klasse der nedarver BaseModel i denne klasse defineres indhold i formen navn: type
### I toppen af filen, definer en liste til at holde de items der er oprettet
### Lav root metoden om til at vise hvor mange items der er, brug metoden len
### Lav read_item metoden om så den bruger item_id til at hente et element fra listen
### Lav en ny metode til at oprette items, som argument skal den tage noget af typen Item, og sætte det i listen, retuner evt. antallet at items i listen
## - Fejlhåndtering i serveren
### Vores read_item metode har mulighed for at lave en fejl, som det er nu giver den fejl men uden en god fejlbesked, det laver vi om så vi får en bedre besked
### Importer status og HTTPException fra fastapi
### En exception kastes med den indbyggede metode raise. I HTTPException sættes status_code f.eks. til status.HTTP_404_NOT_FOUND der kan også sættes en hjelpetekst med argumentet detail 
### Har du lyst til at skrive ekstra dokumentation til dit api kan du gøre det med denne guide https://fastapi.tiangolo.com/tutorial/metadata/
