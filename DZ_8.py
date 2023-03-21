'''
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
'''

phone_book = []
path = 'file.txt'



def open_file(path):
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for contact in data:
            cont = []
            for field in contact.split(';'):
                cont.append(field.strip())
            phone_book.append(cont)



def safe_file():
    file_to_save = []
    with open("file.txt", "w", encoding='UTF8') as file:
    #     file.write(str(phone_book))

        for contact in phone_book:
            dtr_list = []
            for value in contact:
                dtr_list.append(value)
            file_to_save.append(';'.join(dtr_list))

        file.write(str('\n'.join(file_to_save)))
print('изменения сохранены')



def show_contacts(phone_book):
    for i, contact in enumerate(phone_book, 1):
        print(f'{i}. {contact[0]:<20}{contact[1]:<20}{contact[2]:<15}')



def add_contact():
    name = input('Введите имя и фамилию: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    phone_book.append(list([name, phone, comment]))



def change_contact():
    search_ch = input('Введите ключевой элемента контакта : ')
    for contact in phone_book:
        for field in contact:
            if search_ch in field:
                print('Искомый контакт :', contact)
                znachenie = int(input('''
                                    Что вы хотите заменить:'
                                      '1 - имя '
                                      '2 - номер '
                                      '3 - комментарий '
                                      '''''))


                if znachenie == 1:
                    new_name = input('Введите новое Имя: ')
                    contact[0] = new_name
                    print(contact)
                if znachenie == 2:
                    new_num = input('Введите новый номер: ')
                    contact[1] = new_num
                    print(contact)
                if znachenie == 3:
                    new_com = input('Введите новый комментарий: ')
                    contact[2] = new_com
                    print(contact)



def search_contact(phone_book):
    search = input('Введите ключевой элемент : ')
    for contact in phone_book:
        for field in contact:
            if search in field:
                print('Искомый контакт ' , contact)



def delete():
    name_del = input('Введите ключевой элемента контакта : ')
    for contact in phone_book:
        for field in contact:
            if name_del in field:
                print('Искомый контакт :', contact)
                del_cont = int(input('''вы действительно хотите удалить контакт?'
                         'да - 1'
                         'нет - 2'
                         '''))
                if del_cont == 1:
                    phone_book.remove(contact)
                    print("Вы удалили контакт %s " % contact)
                else:
                    print('Выберите другой пункт меню')



while True:
    print('''Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Изменить контакт
    6. Найти контакт
    7. Удалить контакт
    8. Выход''')
    number = int(input('Введите пункт меню: '))

    match number:
        case 1:
            open_file(path)
            print('Файл успешно загружен')
        case 2:
            safe_file()
        case 2:
            pass
        case 3:
            show_contacts(phone_book)
        case 4:
            add_contact()
        case 5:
            change_contact()
        case 6:
            search_contact(phone_book)
        case 7:
            delete()
        case 8:
            break
