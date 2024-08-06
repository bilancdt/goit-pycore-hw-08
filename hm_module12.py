import pickle

class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __str__(self):
        return f"Person(name={self.name}, email={self.email}, phone={self.phone}, favorite={self.favorite})"

class AddressBook:
    def __init__(self, contacts=None):
        if contacts is None:
            contacts = []
        self.contacts = contacts

    def add_person(self, person: Person):
        self.contacts.append(person)

    def remove_person(self, name: str):
        self.contacts = [p for p in self.contacts if p.name != name]

    def find_person(self, name: str):
        for person in self.contacts:
            if person.name == name:
                return person
        return None

    def __str__(self):
        return f"AddressBook(contacts={self.contacts})"

def save_data(address_book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(address_book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повертає нову адресу, якщо файл не знайдено
def main():
    # Завантаження адресної книги
    book = load_data()

    # Основний цикл програми
    while True:
        print("1. Додати контакт")
        print("2. Видалити контакт")
        print("3. Показати контакти")
        print("4. Вийти")
        
        choice = input("Виберіть дію (1/2/3/4): ")

        if choice == "1":
            name = input("Введіть ім'я: ")
            email = input("Введіть email: ")
            phone = input("Введіть телефон: ")
            favorite = input("Улюблений (так/ні): ").lower() == "так"
            person = Person(name, email, phone, favorite)
            book.add_person(person)
        
        elif choice == "2":
            name = input("Введіть ім'я для видалення: ")
            book.remove_person(name)
        
        elif choice == "3":
            print("Контакти:")
            for person in book.contacts:
                print(person)
        
        elif choice == "4":
            # Збереження перед виходом
            save_data(book)
            print("Зміни збережено. Вихід з програми.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")
# запуск
if __name__ == "__main__":
    main()
