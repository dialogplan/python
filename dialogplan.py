import argparse
import os
import yaml


def create_yaml_file(data, filename="dialogplan.yaml"):
    with open(filename, 'w') as file:
        yaml.safe_dump(data, file, sort_keys=False, allow_unicode=True)
    print(f"Plik {filename} został utworzony.")


def interactive_mode():
    project_data = []

    while True:
        etap = input("Podaj nazwę etapu: ")
        czas_wykonania = input("Podaj czas wykonania (np. '3 dni'): ")
        priorytet = input("Podaj priorytet (niski, średni, wysoki): ")
        zależności = input("Podaj zależności (oddzielone przecinkiem, jeśli brak, zostaw puste): ")

        zależności_list = [z.strip() for z in zależności.split(',')] if zależności else []

        project_data.append({
            "etap": etap,
            "czas_wykonania": czas_wykonania,
            "priorytet": priorytet,
            "zależności": zależności_list
        })

        add_more = input("Czy chcesz dodać kolejny etap? (tak/nie): ").lower()
        if add_more != 'tak':
            break

    return project_data


def add_default_step():
    default_step = [{
        "etap": "Tworzenie koncepcji",
        "czas_wykonania": "1h",
        "priorytet": "pilny",
        "zależności": []
    }]
    return default_step


def parse_args():
    parser = argparse.ArgumentParser(description="Tworzenie pliku YAML dla projektu.")
    parser.add_argument("-a", "--add", action="store_true", help="Tryb interaktywny do dodawania etapów.")
    parser.add_argument("--etap", type=str, help="Nazwa etapu")
    parser.add_argument("--czas_wykonania", type=str, help="Czas wykonania etapu (np. '3 dni')")
    parser.add_argument("--priorytet", type=str, choices=['niski', 'średni', 'wysoki', 'pilny'], help="Priorytet etapu")
    parser.add_argument("--zależności", type=str, help="Zależności etapu (oddzielone przecinkiem)")
    return parser.parse_args()


def main():
    args = parse_args()

    # Sprawdzanie czy plik dialogplan.yaml już istnieje
    yaml_file_exists = os.path.exists("dialogplan.yaml")

    if args.add:
        project_data = interactive_mode()

    elif not (args.etap and args.czas_wykonania and args.priorytet):
        if not yaml_file_exists:
            print("Nie podano żadnego etapu i plik dialogplan.yaml nie istnieje.")
            project_data = add_default_step()
        else:
            print("Musisz podać wszystkie parametry: --etap, --czas_wykonania, --priorytet.")
            return
    else:
        zależności_list = [z.strip() for z in args.zależności.split(',')] if args.zależności else []

        project_data = [{
            "etap": args.etap,
            "czas_wykonania": args.czas_wykonania,
            "priorytet": args.priorytet,
            "zależności": zależności_list
        }]

    if yaml_file_exists:
        # Jeśli plik istnieje, wczytaj istniejącą zawartość i dodaj nowe etapy
        with open("dialogplan.yaml", 'r') as file:
            existing_data = yaml.safe_load(file) or []
        project_data = existing_data + project_data

    create_yaml_file(project_data)


if __name__ == "__main__":
    main()