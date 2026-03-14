## Logging
### I python bruges logging til at lave en log over hvad der er sket i programmet</br> Med det formål at finde fejl i program strukturen</br>Mere information kan findes på https://docs.python.org/3/library/logging.html
### I programmet defineres et "log level" hvor meget logging der skal skrives, det er en af følgende levels
logging.DEBUG</br>
logging.INFO</br>
logging.WARNING</br>
logging.ERROR</br>
logging.CRITICAL</br>
### Bemærk at når der skrives til et level så vil log beskeden kunne ses på alle tidligere levels 
### Start med at oprette en python fil med navnet logsetup
### I logsetup importer logging, importer også RotatingFileHandler fra logging.handlers. logging er et standard pyton modul
### Opret en metode kaldet setup_logging eller lignende
### I setup_logging opret et objekt af typen RotatingFileHandler</br>Eller vælg en handler fra listen https://docs.python.org/3.11/library/logging.handlers.html
### Opret et object af typen logging.Formatter dette objekt initialiseres med en formaterings streng, den kan bl.a. indeholde %(asctime)s, %(name)s, %(levelname)s og %(message)s.</br>Se mere på https://docs.python.org/3/library/logging.html#formatter-objects
### Hent root logger med metoden logging.getLogger()
### Sæt level på root loggeren med metoden setLevel
### Tilføj handleren på root loggeren med metoden addHandler
### I toppen af din main metode kan du nu importere din nye logsetup python fil, og herfra kalde setup_logging metoden
### Nu kan du benytte dig af logging setupet ved at importere logging, lave en relevant logger med logger = logging.getLogger(__name__)</br>Bemærk __name__ variablen indeholder forskellig værdi efter hvor i programmet den kaldes fra

