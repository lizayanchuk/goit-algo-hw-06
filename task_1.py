from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10:
            raise ValueError(f"Phone number must be 10 digits, got '{value}'")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone_num):
        self.phones.append(Phone(phone_num))

    def remove_phone(self, phone_num):
        for phone in self.phones:
            if phone.value == phone_num:
                self.phones.remove(phone)
            return f"Phone removed succesfully"

    def edit_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)
        if not phone:
            raise ValueError(f"Phone {old_phone} not found in record {self.name.value}")
        phone.value = new_phone
        return phone

    def find_phone(self, phone_num):
        for phone in self.phones:
            if phone.value == phone_num:
                return phone
        return None

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return None

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        if self.data:
            return "\n".join(str(record) for record in self.data.values())
        else:
            return "No contacts found in the Adress Book"

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі

print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")

print(book)
