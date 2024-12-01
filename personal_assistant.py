import json
from datetime import datetime
import csv

def app_menu() :
     while True:
        print("Добро пожаловать в Персональный помощник!")
        print("Выберите действие:")
        print("1. Управление заметками")
        print("2. Управление задачами")
        print("3. Управление контактами")
        print("4. Управление финансовыми записями")
        print("5. Калькулятор")
        print("6. Выход")

        option = input("Введите номер действия: ")
        if option == '1':
            manage_notes()
        elif option == '2':
            manage_tasks()
        elif option == '3':
            manage_contacts()
        elif option == '4':
            manage_finances()
        elif option == '5':
            calculator()
        elif option == '6':
            break
        else:
            print("Некорректный ввод, попробуйте снова.")

    
class Note:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
        self.timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def manage_notes() :
         while True:
            print("1. Создать новую заметку")
            print("2. Просмотреть все заметки")
            print("3. Просмотреть детали заметки")
            print("4. Редактировать заметку")
            print("5. Удалить заметку")
            print("6. Импортировать заметки из CSV")
            print("7. Экспортировать заметки в CSV")
            print("8. Вернуться в главное меню")

            option = input("Выберите действие: ")

            if option == '1':
                create_note()
            elif option == '2':
                view_notes()
            elif option == '3':
                view_note_details()
            elif option == '4':
                edit_note()
            elif option == '5':
                delete_note()
            elif option == '6':
                export_notes_to_csv()
            elif option == '7':
                import_notes_from_csv()
            elif option == '8':
                break
            else:
                print('Некорректный выбор, попробуйте снова.')
            
        
def create_note():
    notes = load_notes()
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержимое заметки: ")
    note_id = len(notes) + 1
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    new_note = {
        'id': note_id,
        'title': title,
        'content': content,
        'timestamp': timestamp
    }

    notes.append(new_note)
    save_notes(notes)
    print("Заметка успешно создана!")

def view_notes():
    notes = load_notes()
    if not notes:
        print("Нет доступных заметок.")
        return

    for note in notes:
        print(f"{note['id']}: {note['title']} (Создано: {note['timestamp']})")


def load_notes(): 
    try:
        with open('notes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file)

def view_note_details(note_id): 
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            print(f"Заголовок: {note['title']}")
            print(f"Содержимое: {note['content']}")
            print(f"Дата и время: {note['timestamp']}")
            return
    print("Заметка с заданным id не найдена.")


def edit_note(): 
    notes = load_notes()
    note_id = int(input("Введите ID заметки для редактирования: "))

    for note in notes:
        if note['id'] == note_id:
            new_title = input("Введите новый заголовок (оставьте пустым, чтобы не менять): ")
            new_content = input("Введите новое содержимое (оставьте пустым, чтобы не менять): ")

            if new_title:
                note['title'] = new_title
            if new_content:
                note['content'] = new_content

            note['timestamp'] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована!")
            return

    print("Заметка не найдена.")


def delete_note():
    notes = load_notes()
    note_id = int(input("Введите ID заметки для удаления: "))

    for i, note in enumerate(notes):
        if note['id'] == note_id:
            del notes[i]
            save_notes(notes)
            print("Заметка успешно удалена!")
            return

    print("Заметка с заданным id не найдена.")


def import_notes_from_csv(): 
    filename = input("Введите имя файла для импорта (например, notes.csv): ")

    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            notes = load_notes()

            for row in reader:
                row['id'] = len(notes) + 1
                row['timestamp'] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                notes.append(row)

            save_notes(notes)
            print("Заметки успешно импортированы!")

    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Ошибка при импорте: {e}")


def export_notes_to_csv(): 
    filename = input("Введите имя файла для экспорта (например, notes.csv): ")

    notes = load_notes()

    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'title', 'content', 'timestamp'])
        writer.writeheader()

        for note in notes:
            writer.writerow(note)

    print("Заметки успешно экспортированы!")


def manage_tasks():
    while True:
        print("1. Создать новую задачу")
        print("2. Просмотреть все задачи")
        print("3. Отметить задачу как выполненную")
        print("4. Редактировать задачу")
        print("5. Удалить задачу")
        print("6. Импортировать задачи из CSV")
        print("7. Экспортировать задачи в CSV")
        print("8. Вернуться в главное меню")

        option = input("Выберите действие: ")

        if option == '1':
            create_task()
        elif option == '2':
            view_tasks()
        elif option == '3':
            mark_task_done()
        elif option == '4':
            edit_task()
        elif option == '5':
            delete_task()
        elif option == '6':
            import_tasks_from_csv()
        elif option == '7':
            export_tasks_to_csv()
        elif option == '8':
            break
        else:
            print("Некорректный ввод, попробуйте снова.")


class Task:
    def __init__(self, id, title, description='', done=False, priority='Низкий', due_date=None):
        self.id = id
        self.title = title
        self.description = description
        self.done = done
        self.priority = priority
        self.due_date = due_date


def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)



def create_task():
    tasks = load_tasks()
    title = input("Введите название задачи: ")
    description = input("Введите описание задачи: ")
    priority = input("Введите приоритет задачи (Высокий/Средний/Низкий): ")
    due_date = input("Введите срок выполнения задачи (ДД-ММ-ГГГГ): ")

    task_id = len(tasks) + 1  
    new_task = {
        'id': task_id,
        'title': title,
        'description': description,
        'done': False,
        'priority': priority,
        'due_date': due_date
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print("Задача успешно создана!")


def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Нет доступных задач.")
        return

    for task in tasks:
        status = "Выполнена" if task['done'] else "Не выполнена"
        print(
            f"{task['id']}: {task['title']} (Статус: {status}, Приоритет: {task['priority']}, Срок: {task['due_date']})")



def mark_task_done():
    tasks = load_tasks()
    task_id = int(input("Введите ID задачи, которую хотите отметить как выполненную: "))

    for task in tasks:
        if task['id'] == task_id:
            task['done'] = True
            save_tasks(tasks)
            print("Задача успешно отмечена как выполненная!")
            return

    print("Задача c заданным id найдена.")


def edit_task():
    tasks = load_tasks()
    task_id = int(input("Введите ID задачи для редактирования: "))

    for task in tasks:
        if task['id'] == task_id:
            new_title = input("Введите новое название (оставьте пустым, чтобы не менять): ")
            new_description = input("Введите новое описание (оставьте пустым, чтобы не менять): ")
            new_priority = input("Введите новый приоритет (оставьте пустым, чтобы не менять): ")
            new_due_date = input("Введите новый срок выполнения (ДД-ММ-ГГГГ, оставьте пустым, чтобы не менять): ")

            if new_title:
                task['title'] = new_title
            if new_description:
                task['description'] = new_description
            if new_priority:
                task['priority'] = new_priority
            if new_due_date:
                task['due_date'] = new_due_date

            save_tasks(tasks)
            print("Задача успешно отредактирована!")
            return

    print("Задача c заданным id не найдена.")



def delete_task():
    tasks = load_tasks()
    task_id = int(input("Введите ID задачи для удаления: "))

    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            del tasks[i]
            save_tasks(tasks)
            print("Задача успешно удалена!")
            return

    print("Задача c заданным id не найдена.")



def import_tasks_from_csv():
    filename = input("Введите имя файла для импорта (например, tasks.csv): ")

    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            tasks = load_tasks()

            for row in reader:
                row['id'] = len(tasks) + 1  
                row['done'] = False 
                tasks.append(row)

            save_tasks(tasks)
            print("Задачи успешно импортированы!")

    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Ошибка при импорте: {e}")



def export_tasks_to_csv():
    filename = input("Введите имя файла для экспорта (например, tasks.csv): ")

    tasks = load_tasks()

    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'title', 'description', 'done', 'priority', 'due_date'])
        writer.writeheader()

        for task in tasks:
            writer.writerow(task)

    print("Задачи успешно экспортированы!")


def manage_contacts(): 
    while True:
        print("1. Создать новый контакт")
        print("2. Просмотреть все контакты")
        print("3. Редактировать контакт")
        print("4. Удалить контакт")
        print("5. Импортировать контакты из CSV")
        print("6. Экспортировать контакты в CSV")
        print("7. Вернуться в главное меню")

        options = input("Выберите действие: ")

        if options == '1':
            create_contact()
        elif options == '2':
            view_contacts()
        elif options == '3':
            edit_contact()
        elif options == '4':
            delete_contact()
        elif options == '5':
            import_contacts_from_csv()
        elif options == '6':
            export_contacts_to_csv()
        elif options == '7':
            break
        else:
            print("Некорректный ввод, попробуйте снова.")


class Contact:
    def __init__(self, id, name, phone='', email=''):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email


def load_contacts(): 
    try:
        with open('contacts.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_contacts(contacts): 
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)


def create_contact(): 
    contacts = load_contacts()
    name = input("Введите имя контакта: ")
    phone = input("Введите номер телефона: ")
    email = input("Введите адрес электронной почты: ")

    contact_id = len(contacts) + 1 
    new_contact = {
        'id': contact_id,
        'name': name,
        'phone': phone,
        'email': email
    }

    contacts.append(new_contact)
    save_contacts(contacts)
    print("Контакт успешно создан!")


def view_contacts(): 
    contacts = load_contacts()
    if not contacts:
        print("Нет доступных контактов.")
        return

    for contact in contacts:
        print(f"{contact['id']}: {contact['name']} (Телефон: {contact['phone']}, Email: {contact['email']})")


def edit_contact():
    contacts = load_contacts()
    contact_id = int(input("Введите ID контакта для редактирования: "))

    for contact in contacts:
        if contact['id'] == contact_id:
            new_name = input("Введите новое имя (оставьте пустым, чтобы не менять): ")
            new_phone = input("Введите новый номер телефона (оставьте пустым, чтобы не менять): ")
            new_email = input("Введите новый адрес электронной почты (оставьте пустым, чтобы не менять): ")

            if new_name: contact['name'] = new_name
            if new_phone: contact['phone'] = new_phone
            if new_email: contact['email'] = new_email

            save_contacts(contacts)
            print("Контакт успешно отредактирован!")
            return

    print("Контакт с заданным id не найден.")


def delete_contact():
    contacts = load_contacts()
    contact_id = int(input("Введите ID контакта для удаления: "))

    for i, contact in enumerate(contacts):
        if contact['id'] == contact_id:
            del contacts[i]
            save_contacts(contacts)
            print("Контакт успешно удален!")
            return

    print("Контакт с заданным id не найден.")


def import_contacts_from_csv():
    filename = input("Введите имя файла для импорта (например, contacts.csv): ")

    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            contacts = load_contacts()

            for row in reader:
                row['id'] = len(contacts) + 1  
                contacts.append(row)

            save_contacts(contacts)
            print("Контакты успешно импортированы!")

    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Ошибка при импорте: {e}")


def export_contacts_to_csv(): 
    filename = input("Введите имя файла для экспорта (например, contacts.csv): ")

    contacts = load_contacts()

    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'name', 'phone', 'email'])
        writer.writeheader()

        for contact in contacts:
            writer.writerow(contact)

    print("Контакты успешно экспортированы!")


def manage_contacts(): 
    while True:
        print("\n--- Управление Контактами ---")
        print("1. Создать новый контакт")
        print("2. Просмотреть все контакты")
        print("3. Редактировать контакт")
        print("4. Удалить контакт")
        print("5. Импортировать контакты из CSV")
        print("6. Экспортировать контакты в CSV")
        print("7. Вернуться в главное меню")

        choice = input("Выберите действие: ")

        if choice == '1':
            create_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            edit_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            import_contacts_from_csv()
        elif choice == '6':
            export_contacts_to_csv()
        elif choice == '7':
            break
        else:
            print("Некорректный ввод, попробуйте снова.")



class FinanceRecord:
    def __init__(self, id, amount, category='', date='', description=''):
        self.id = id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description


def load_finances(): 
    try:
        with open('finance.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_finances(finances):
    with open('finance.json', 'w') as file:
        json.dump(finances, file)


def create_finance_record(): 
    finances = load_finances()

    amount = float(input("Введите сумму операции: "))
    category = input("Введите категорию операции (например, Еда): ")
    date = input("Введите дату операции (ДД-ММ-ГГГГ): ")
    description = input("Введите описание операции: ")

    finance_id = len(finances) + 1  
    new_record = {
        'id': finance_id,
        'amount': amount,
        'category': category,
        'date': date,
        'description': description
    }


    finances.append(new_record)
    save_finances(finances)
    print("Финансовая запись успешно создана!")


def view_finance_records(): 
    finances = load_finances()
    if not finances:
        print("Нет доступных финансовых записей.")
        return

    for record in finances:
        print(
            f"{record['id']}: {record['description']} (Сумма: {record['amount']}, Категория: {record['category']}, Дата: {record['date']})")
        

def import_finance_records_from_csv(): 
    filename = input("Введите имя файла для импорта (например, finance.csv): ")

    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            finances = load_finances()

            for row in reader:
                row['id'] = len(finances) + 1
                row['amount'] = float(row['amount'])
                finances.append(row)

            save_finances(finances)
            print("Финансовые записи успешно импортированы!")

    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Ошибка при импорте: {e}")


def export_finance_records_to_csv(): 
    filename = input("Введите имя файла для экспорта (например, finance.csv): ")

    finances = load_finances()

    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'amount', 'category', 'date', 'description'])
        writer.writeheader()

        for record in finances:
            writer.writerow(record)

    print("Финансовые записи успешно экспортированы!")

def manage_finances(): 
    while True:
        print("\n--- Управление Финансовыми Записями ---")
        print("1. Добавить новую финансовую запись")
        print("2. Просмотреть все записи")
        print("3. Импортировать записи из CSV")
        print("4. Экспортировать записи в CSV")
        print("5. Вернуться в главное меню")

        choice = input("Выберите действие: ")

        if choice == '1':
            create_finance_record()
        elif choice == '2':
            view_finance_records()
        elif choice == '3':
            import_finance_records_from_csv()
        elif choice == '4':
            export_finance_records_to_csv()
        elif choice == '5':
            break
        else:
            print("Некорректный ввод, попробуйте снова.")

def calculator(): 
   while True:
       expression = input("\nВведите арифметическое выражение (или введите 'выход' для выхода): ")
       if expression.lower() == "выход":
           break

       try:
           result = eval(expression)
           print(f"Результат: {result}")
       except ZeroDivisionError:
           print("Ошибка: деление на ноль.")
       except Exception as e:
           print(f"Ошибка при вычислении выражения: {e}")


if __name__ == "__main__":
   app_menu()