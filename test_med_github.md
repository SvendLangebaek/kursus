# Test med github
## Opret tests
### Målet med dette er at opsætte en automatisk test, der sikre at der ikke bliver frigivet kode med fejl
### Opret branch til dette, kald den f.eks. test
### Installer modulet pytest
### Lav en mappe med navnet "tests"
### Lav en python fil hvor navnet starter med test i mappen tests
### Indsæt følgende kode

```
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
```

### Eksemplet er taget fra https://docs.pytest.org/en/stable/getting-started.html Læs gerne mere der
### Kør testen i pycharm er der en kør icon ud for metoden, ellers kan den køres med

```
python -m pytest tests/
```

## Få github til at udføre din test
### For at github kan lave testen automatisk skal der findes en liste over dependencies</br>For uv er det filerne pyproject.toml, .python-version og uv.lock</br>For pip er det filen requirements.txt</br>Både uv og pip kan generere requirements.txt med freeze kommandoen
### Opret mappestrukturen .github/workflows
### I .github/workflows opret en fil af typen yaml eller yml
### Brug et af eksemplerne i https://github.com/SvendLangebaek/kursus/tree/test/.github/workflows til start</br>Se evt. andre workflow actions på https://github.com/marketplace?type=actions
### push til git og se om github fanger testen
