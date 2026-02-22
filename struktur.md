# Hvordan skal jeg organisere mit python projekt?

## Ting til Tanker
### ! Brug git til versions styring
### ! Lav en README.md til den der skal bruge dit projekt, have et helt simpelt "hello world" eksempel
### ! Små filer, Små klasser, Små metoder
### ! Tænk over hvilke klasser der har ansvar for hvad
### ! Brug lsp (indbygget i pycharm og vscode) f.eks. pyright
### ! Tænk over om metoders navne er dokumentation nok eller der er behov for kommentar
### ! Pas på cirkulær imports, generelt gå efter kun at importere dybere i stien
### ! Lav ikke dit projekt alene, har du ikke nogen at kode med så få feedback
### ! Søg gerne på "buzz words" der forklare nogle af principperne "high cohesion low coupling", "Clean Code", "Code Patterns", "Code Smells"/"Anti Pattern" Eller læs python PEP på https://peps.python.org/ f.eks. https://peps.python.org/pep-0020/
### ! Og aller mest vigtigt: dit projekt, dit design.


## Projektmappe eksempel, dette et eksempel på hvordan strukturen i et python projekt kunne være

```text
projekt_mappe/
│
├── visning/
│   ├── Illustrator.py
│   └── billeder/
│       ├── hund.jpeg
│       └── kat.jpeg
│
├── data/
│   ├── Hund.py
│   └── Kat.py
│
├── tests
│   └── visning/
│       └── TestIllustrator.py
│
├── main.py
└── .gitignore
```
##

