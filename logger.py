import os

def input_contact():
    # f = open('data.txt', 'r')
    # if not f:
    #     f = open('data.txt', 'w')
    #     f.close()
    # else:
    #     f.close()
    if not os.path.isfile('data.txt'):
        f = open('data.txt', 'w')
        f.close()


    with open('data.txt', 'a', encoding='utf-8') as f:
        user = input('Введите имя, фамилию и телефон: ').strip().split()
        f.write(';'.join(user) + '\n')


def print_contacts():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    for contact in contacts:
        print(*contact.strip().split(';'))


def find_contact():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    while True:
        print('По каким параметрам ищем контакт?:\n1. Имя\n2. Фамилия\n3. Телефон')
        command_index = int(input('Команда: '))
        if str(command_index) not in '123':
            print('Других параметров нету.')
        else:
            break
    data = input('Введите данные: ')
    print('Найденные контакты: ')
    for contact in contacts:
        full_contact = contact.strip().split(';')
        if data == full_contact[command_index-1]:
            print(' '.join(full_contact))

def change_contact():
    with open('data.txt', 'r+', encoding='UTF8') as f:
        contacts = f.readlines()
        while True:
            choice = input("для поиска по имени нажмите - 0 " \
            'Для поиска по фамилии нажмите - 1 \n Для поска по номеру нажмите - 2 \n')
            if choice not in '012':
                print('Других данных нет!!!')
            else:
                choice = int(choice)
                if choice == 0:
                    name = "Введите имя: "
                elif choice == 1:
                    name = "Ведите фамилию: "
                elif choice == 2:
                    name = "Введите номер телефона: "
                break
        surnami = input(f'{name}')
        id = 0
        count = 0
        print("Найденные контакты: \n")
        print('id   Контакт')
        for contact in contacts:
            ful_contact = contact.strip().split(',')
            if surnami.lower() == ful_contact[choice].lower():
                print(id + 1, *ful_contact)
                count += 1
            id =+ 1
        if not count == 0:
            id_inp = int(input("Введите id редактируемого контакта: ")) -1
            new_text = input("Введите, имя, фамилию, номер телефона с изменениями:  ").strip().split()
            contacts[id_inp ] = ','.join(new_text) + '\n'
            f.seek(0)
            f.writelines(contacts) 
        else:
            print("Контакт не найден")


def delete_contact():
    with open('data.txt', 'r+', encoding='UTF8') as f:
        contacts = f.readlines()
        id = 0
        for contact in contacts:
             print((id + 1), *contact.strip().split(','))
             id += 1
        del_lines = int(input("Введите номер строки для удаления: ")) - 1
        with open('data.txt', 'w', encoding='UTF8') as f:
            del_txt = contacts[del_lines].strip()
            for contact in contacts:
                if contact.strip() != del_txt:
                    f.write(contact)
            print("Строка успешно удалена")


