import csv
import os

FILENAME = "telefonbok.csv"

def clear_screen():
    os.system("cls")

def pause():
    input("\nTryck Enter för att fortsätta...")

def load_from_csv():
    people = []
    if os.path.exists(FILENAME):
        with open(FILENAME, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if 'anteckningar' not in row:
                    row['anteckningar'] = ""
                people.append(row)
    return people

def save_to_csv(people):
    with open(FILENAME, "w", newline="", encoding="utf-8") as file:
        fields = ["namn", "mobil", "anteckningar"]
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(people)

def show_list(people):
    if not people:
        print("Listan är tom.")
        return
    for i, person in enumerate(people, 1):
        print(f"{i}. {person['namn']}")

def sort_list(people):
    people.sort(key=lambda p: p['namn'].lower())
    
def add_person(people):
    name = input("Ange namn: ")
    mobile = input("Ange mobilnummer: ")
    notes = input("Ange anteckningar: ")


    people.append({
        "namn": name,
        "mobil": mobile,
        "anteckningar": notes
    })

    sort_list(people)
    save_to_csv(people)
    print("Person tillagd!")
    pause()
    
def show_details(people):
    show_list(people)
    if not people:
        pause()
        return
    try:
        choice = int(input("Välj person (nummer): ")) - 1
        person = people[choice]
        print("\n--- Detaljer ---")
        print(f"Namn: {person['namn']}")
        print(f"Mobil: {person['mobil']}")
        print(f"Anteckningar: {person.get('anteckningar', '')}")
    except (ValueError, IndexError):
        print("Ogiltigt val.")
        pause()
        
def edit_person(people):
    show_list(people)
    if not people:
        pause()
        return

    try:
        choice = int(input("Välj person att redigera: ")) - 1
        person = people[choice]
        new_name = input(f"Nytt namn ({person['namn']}): ")
        new_mobile = input(f"Nytt mobilnummer ({person['mobil']}): ")
        new_notes = input(f"Nya anteckningar ({person.get('anteckningar', '')}): ")

        if new_name:
            person['namn'] = new_name
        if new_mobile:
            person['mobil'] = new_mobile
        if new_notes:
            person['anteckningar'] = new_notes

        sort_list(people)
        save_to_csv(people)
        print("Person uppdaterad!")
    except (ValueError, IndexError):
        print("Ogiltigt val.")
    pause()
    
def delete_person(people):
    show_list(people)
    if not people:
        pause()
        return

    try:
        choice = int(input("Välj person att ta bort: ")) - 1
        removed = people.pop(choice)
        print(f"{removed['namn']} har tagits bort.")
        save_to_csv(people)
    except (ValueError, IndexError):
        print("Ogiltigt val.")
    pause()
    
def main():
    people = load_from_csv()

    while True:
        os.system("cls")
        clear_screen()

        sort_list(people)

        print("\n--- Kontaktlista ---")
        show_list(people)

        print("\nMeny:")
        print("(L) Lägg till person")

        
if __name__ == "__main__":
    main()