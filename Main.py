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