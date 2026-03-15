## Profiling og Performance https://docs.python.org/3/library/profile.html
### I python er der indbyggede metoder til at profilere et program</br>Dette bruges hvis man opdager at der er steder i programmet der tager meget lang tid i forhold til hvad de burde
## 1. Test enkelte metoder denne metode bruges for at afdække hvad der tager lang tid de tager
### I jupyter notebook importer cProfile (eller profile hvis du ikke har cProfile)
### En metode testes med cProfile.run metoden.</br> Metoden tager statement argumentet som er en string med den python kode der skal testes</br>Derudover kan man vælge også at bruge sort argumentet der fortæller hvordan resultatet sorteres, f.eks. tottime eller cumtime.</br>Hint pak gerne kode ind i en metode, det gør det nemmere at overskue 
### Opgave, brug run metoden til at finde ud af om det er hurtigst at gøre x**2 eller x*x for en række af tal (brug gerne den indbyggede range metode)
### Opgave, brug run metoden til at finde ud af om det er hurtigst at bygge en liste op i en for løkke eller i list comprehension
## 2. Test et python program. Denne metode bruges til at identificere hvilke dele af et program der tager lang tid
### Åben en command line og brug kommandoen</br>python -m cProfile [-o output_file] [-s sort_order] (-m module | myscript.py)</br>Bruger du uv så sæt uv run foran</br>
### Herefter Kan indholdet af output filen læses med</br> python -m pstats output_file</br>Brug "help" commandoen til at se hvad du kan i pstats
### Opgave, hvad tager længst tid i dit program?
