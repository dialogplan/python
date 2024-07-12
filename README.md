# [python.dialogplan.com](http://python.dialogplan.com)

## Cel projektu

Skrypt:
+ inicjuje
+ waliduje
+ tworzył plik YAML 
na podstawie interaktywnych podpowiedzi 


### Sposoby wykonania skryptu:

#### Tryb interaktywny:
W trybie interaktywnym użytkownik może uruchomić skrypt i będzie mógł dodawać etapy projektu jeden po drugim:

```bash
python dialogplan.py -a
```

#### Tryb poprzez linię poleceń:

W tym trybie użytkownik może podać wszystkie parametry jednorazowo w linii poleceń. Na przykład, aby dodać jeden etap:

```bash
python dialogplan.py --etap "Analiza wymagań" --czas_wykonania "3 dni" --priorytet "wysoki" --zależności ""
```

**Note:** Plik zapisywany jest domyślnie jako `dialogplan.yaml` w bieżącym katalogu. Możesz zmienić nazwę pliku w funkcji `create_yaml_file`, jeśli to konieczne.

### Wyjaśnienie skryptu:

1. **create_yaml_file**: Funkcja zapisująca dane do pliku YAML.
2. **interactive_mode**: Funkcja obsługująca interaktywny sposób dodawania etapów.
3. **parse_args**: Funkcja parsująca argumenty z linii poleceń.
4. **main**: Główna funkcja, która uruchamia odpowiedni tryb działania w zależności od podanych argumentów.





## dialogplan bash


Skrypt bash `dialogplan` automatycznie przekazuje odpowiednie parametry do skryptu Pythona `dialogplan.py`, uruchamiając go w trybie interaktywnym lub z linią poleceń na podstawie dostarczonych argumentów.


### Start

1. Upewnij się, że skrypt Pythona `dialogplan.py` znajduje się w tym samym katalogu co `dialogplan`.
2. Nadaj skryptowi wykonawczych uprawnień:

```bash
chmod +x dialogplan
```


### Jak używać skryptu bash `dialogplan`?

```bash
./dialogplan
```

1. **Tryb interaktywny**:

```bash
./dialogplan -a
```

2. **Podanie parametrów w linii poleceń**:

```bash
./dialogplan --etap "Analiza wymagań" --czas_wykonania "3 dni" --priorytet "wysoki" --zależności ""
```


