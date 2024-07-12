# [python.dialogplan.com](http://python.dialogplan.com)

## Cel projektu

Skrypt:
+ inicjuje
+ waliduje
+ tworzył plik YAML 
na podstawie interaktywnych podpowiedzi 


## jak to dziala

Dialogware:
- dialog**stream** - komunikacja ze wszystkimi aktorami i maszynami w celu zebrania wymaga i postepow i uruchomienia na serwerze w czasie rzeczywistym
   - zapisuje dane do dialogstory, dialogchain
- dialog**story** - opisy funkcji napisane z perspektywy użytkownika końcowego.
  - zbieranie wymaga klienta
- dialog**plan** - plan wykonania projektu, uwzgledniajcy milestones, deadlines, estimates, priority
  - bazuje na dialogstory
- dialog**path** - scenariusze wykonania projektu w zaleznosci od osoby i implementacji
  - bazuje na dialogplan i dialogstory 
- dialo**graph** - graficzna reprezentacja roznych scenariuszy, mermaid roadmap
  - bazuje na dialogplan i dialogpath 
- dialog**chain** - lancuch transakcji wykorzystania zasobow przez aktorow, np. rozliczenie godzin pracy, kontraktow, oprogramowania, pracy ludzi i maszyn.
  - bazuje na wszystkim elementach, zapisuje wszystkie zdarzenia w organizacji i transakcje  


dialograph ma pokazywac stan projektu + mermaid + roadmpan+ integracja, koszt, czas, zasoby

dialogchain 

      - debt: 1-5
      - complex: 0 .. 5
      -
      - human:
      - hour: 50

## menu

+ [PERT – Wikipedia, wolna encyklopedia](https://pl.wikipedia.org/wiki/PERT)

[PERT – Wikipedia, wolna encyklopedia](https://pl.wikipedia.org/wiki/PERT)

> **PERT** ([ang.](https://pl.wikipedia.org/wiki/J%C4%99zyk_angielski "Język angielski") _Program Evaluation and Review Technique_) – probabilistyczna metoda planowania i kontroli [projektu](https://pl.wikipedia.org/wiki/Projekt_(zarz%C4%85dzanie) "Projekt (zarządzanie)"), wykorzystująca [programowanie sieciowe](https://pl.wikipedia.org/wiki/Programowanie_sieciowe "Programowanie sieciowe"), stosowana w [zarządzaniu projektami](https://pl.wikipedia.org/wiki/Zarz%C4%85dzanie_projektem "Zarządzanie projektem").
> 
> 
> 

### Sposoby wykonania skryptu:

#### Tryb interaktywny:
W trybie interaktywnym użytkownik może uruchomić skrypt i będzie mógł dodawać etapy projektu jeden po drugim:

```bash
python dialogware.py -a
```

#### Tryb poprzez linię poleceń:

W tym trybie użytkownik może podać wszystkie parametry jednorazowo w linii poleceń. Na przykład, aby dodać jeden etap:

```bash
python dialogware.py --etap "Analiza wymagań" --czas_wykonania "3 dni" --priorytet "wysoki" --zależności ""
```

**Note:** Plik zapisywany jest domyślnie jako `dialogplan.yaml` w bieżącym katalogu. Możesz zmienić nazwę pliku w funkcji `create_yaml_file`, jeśli to konieczne.

### Wyjaśnienie skryptu:

1. **create_yaml_file**: Funkcja zapisująca dane do pliku YAML.
2. **interactive_mode**: Funkcja obsługująca interaktywny sposób dodawania etapów.
3. **parse_args**: Funkcja parsująca argumenty z linii poleceń.
4. **main**: Główna funkcja, która uruchamia odpowiedni tryb działania w zależności od podanych argumentów.



jeśli żaden etap nie zostanie podany, to plik `dialogplan.yaml` zostanie utworzony 


1. **Sprawdzenie istnienia pliku** `dialogplan.yaml`: Skrypt sprawdza, czy plik YAML istnieje.
2. **Tryb interaktywny**: Jeśli użyto opcji `-a`, skrypt uruchomi tryb interaktywny.
3. **Brak parametrów w linii poleceń**: Jeśli nie podano żadnych parametrów i plik `dialogplan.yaml` nie istnieje, skrypt doda domyślny etap do nowego pliku.
4. **Podanie parametrów w linii poleceń**: Jeśli podano





### Jak to działa:
1. **Funkcja `create_yaml_file`**: Zapisuje dane do pliku YAML.
2. **Funkcja `update_history`**: Zapisuje historię zmian do pliku `dialoghistory.yaml`.
3. **Funkcja `interactive_mode`**: Umożliwia użytkownikowi dodawanie etapów w trybie interaktywnym.
4. **Funkcja `add_default_step`**: Dodaje domyślny etap, jeśli nie podano parametrów i plik `dialogplan.yaml` nie istnieje.
5. **Funkcja `parse_args`**: Parsuje argumenty z linii poleceń.
6. **Funkcja `main`**:
   - **Interaktywny tryb**: Uruchamia tryb interaktywny i zapisuje historię zmian.
   - **Brak parametrów**: Dodaje domyślny etap, jeśli nie podano żadnych parametrów, a plik `dialogplan.yaml` nie istnieje, i zapisuje to w historii.
   - **Podanie parametrów w linii poleceń**: Dodaje etap na podstawie podanych parametrów i zapisuje historię zmian.
   - **Aktualizacja istniejących danych**: Jeśli plik istnieje, nowe dane są dołączane do istniejących.

Za pomocą tego skryptu możesz śledzić historię zmian w pliku `dialoghistory.yaml`, co pozwala na lepsze zarządzanie projektem i monitorowanie zmian w etapach projektu.





## dialogplan bash


Skrypt bash `dialogplan` automatycznie przekazuje odpowiednie parametry do skryptu Pythona `dialogware.py`, uruchamiając go w trybie interaktywnym lub z linią poleceń na podstawie dostarczonych argumentów.


### Start

1. Upewnij się, że skrypt Pythona `dialogware.py` znajduje się w tym samym katalogu co `dialogplan`.
2. Nadaj skryptowi wykonawczych uprawnień:

```bash
chmod +x dialogplan
```


### Jak używać skryptu bash `dialogplan`?

```bash
./dialogware
```

1. **Tryb interaktywny**:

```bash
./dialogware -a
```

2. **Podanie parametrów w linii poleceń**:

```bash
./dialogware --etap "Analiza wymagań" --czas_wykonania "3 dni" --priorytet "wysoki" --zależności ""
```

```yaml
  - etap: "Analiza wymagań"
    czas_wykonania: "3 dni"
    priorytet: "wysoki"
    zależnosci: []

  - etap: "Projektowanie systemu"
    czas_wykonania: "5 dni"
    priorytet: "średni"
    zależnosci: ["Analiza wymagań"]

  - etap: "Implementacja"
    czas_wykonania: "10 dni"
    priorytet: "wysoki"
    zależnosci: ["Projektowanie systemu"]

  - etap: "Testowanie"
    czas_wykonania: "7 dni"
    priorytet: "wysoki"
    zależnosci: ["Implementacja"]

  - etap: "Wdrożenie"
    czas_wykonania: "2 dni"
    priorytet: "wysoki"
    zależnosci: ["Testowanie"]
```


## dialoghistory 
opisanie historii zmian dotyczącej projektu. 

### Wyjaśnienie:
- **dialog**: prefix sugerujący, że zawartość dotyczy interakcji, komunikacji lub procesów zarejestrowanych w celu organizacji projektu.
- **story**: drugi człon określający, że dokument zawiera historię zmian, aktualizacje lub inne istotne wydarzenia związane z projektem.

`dialoghistory.yaml` może zawierać szczegóły na temat każdej zmiany w projekcie, w tym daty zmian, kto dokonał zmiany, czym zmiana była i dlaczego była konieczna.
```yaml
zmiany:
  - data: "2023-01-10"
    kto: "Jan Kowalski"
    opis: "Dodanie etapu 'Analiza wymagań'"
  - data: "2023-01-12"
    kto: "Anna Nowak"
    opis: "Zmiana priorytetu etapu 'Projektowanie systemu' na 'wysoki'"
  - data: "2023-01-15"
    kto: "Piotr Wiśniewski"
    opis: "Dodanie zależności do etapu 'Implementacja'"
  - data: "2023-01-20"
    kto: "Magdalena Zielińska"
    opis: "Zmiana czasu wykonania etapu 'Testowanie' z 5 dni na 7 dni"
```