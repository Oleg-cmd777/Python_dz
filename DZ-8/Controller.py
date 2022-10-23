import Model
import View



def start():


    def main_menu():

        while True:
            print('\nГлавное меню:')
            print('1 Показать все контакты')
            print('2 Открыть файл контактов')
            print('3 Записать в файл контакт')
            print('4 Поиск контакта')
            print('5 Добавить контакт')
            print('6 Удалить контакт')
            print('7 Изменить контакт')
            print('8 Сохранить файл')
            print('0. Выйти из программы')
            choice = int(input('Выберите пункт: '))
            match (choice):
                case 1:
                    view_contact()
                    print('\nКонтакт просмотрен\n')
                case 2:
                    open_contact()
                    print('\nКонтакт открыт\n')
                case 3:
                    write_contact()
                    print('\nЗапись добавлен\n')
                case 4:
                    search_contact()
                    print('\nПоиск контакта\n')
                case 5:
                    add_contact()
                    print('\nКонтакт добавлен\n')
                case 6:
                    remove_contact()
                    print('\nКонтакт удален\n')
                case 7:
                    change_contact()
                    print('\nКонтакт изменен\n')
                case 8:
                    save_file()
                    print('\nФайл сохранен!\n')
                case 0:
                    break


    print(main_menu())

# def start():
#     open_file()
#     View.printPhoneBook()
#     main_menu()

def view_contact():
    with open("phon.txt", encoding="utf8") as data:
        # s = data.readline()
        # print(s)
        for line in data:
            line = line.strip()
            print(line)

def open_contact():
    with open("phon.txt", encoding="utf8") as data:
        m = data.readline()
        print(m)


def write_contact():
    with open("writephone.txt", "w", encoding="utf8") as data:
        n = data.write("Вася, телефона нет")
        print(n)


def  search_contact():
    nname = input("Введи имя контакта  ")
    with open("phon.txt", encoding="utf8") as data:
        # s = data.readline()
        # print(s)
        for line in data:
            if nname in line:

                print(line)

def add_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    last_name = input('Введите отчество: ')
    phone = input('Введите телефон: ')
    contact = f'{name}; {surname}; {last_name}; {phone};\n'
    Model.phonebook.append(contact)
    print(Model.phonebook)

def remove_contact():
    choice = int(input('Введите номер элемента для удаления: '))
    Model.phonebook.pop(choice)
    print(Model.phonebook)


def change_contact():

    choice = int(input('Введите номер элемента для изменения: '))
    choice2 = int(input('Что изменяем (0-имя, 1-фамилия, 2-отчество, 3-телефон): '))

    contact = Model.phonebook.pop(choice).split(';')
    print(contact)
    contact[choice2] = input('Введите новое значение: ')
    print(contact)
    Model.phonebook.insert(choice, ';'.join(contact))
    print(Model.phonebook)



def save_file():
    print("Файл сохранен")

