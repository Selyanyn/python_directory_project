import os

def get_path_to_directory(directory_name):
    return f"directories/{directory_name}.txt"

def transform_record_into_list(record):
    if (not record):
        return False
    record_info = record.split(' ')
    if (len(record_info) != 5):
        return False
    return record_info

def create_directory(name):
    file = open(get_path_to_directory(name), "w+")
    return file

def create_record(directory_name, record_info):
    PATH = get_path_to_directory(directory_name)
    if (not record_info) : return
    file = open(PATH, 'r')
    if (not find_record(file, record_info)):
        file.close()
        file = open(PATH, 'a')
        file.write(" ".join(record_info) + '\n')
    else:
        print(f"Запись с {record_info[4]} уже присутствует в {directory_name}!")
    file.close()

def find_record(file, info):
    for line in file.readlines():
        current_record = line.split(' ')
        if (info[2] == current_record[2] or info[4] == current_record[4][:-1]):
            return(line)
    return False

def replace_or_remove_record(directory_name, info, new_info = ""):
    PATH = get_path_to_directory(directory_name)
    file = open(PATH, 'r')
    result = ""
    for line in file:
        current_record = line.split(' ')
        if (not (info == current_record[2] or info == current_record[4][:-1]) and
                (new_info[2] == current_record[2] or new_info[4] == current_record[4][:-1])):
            file.close()
            print("Новая информация не является уникальной в директории!")
            return False
        if (info == current_record[2] or info == current_record[4][:-1]):
            if (new_info):
                line = " ".join(new_info) + '\n'
            else:
                line = ""
        result += line
    file.close()
    file = open(PATH, 'w')
    file.write(result)

def read_directory(name):
    file = open(get_path_to_directory(name), 'r')
    for line in file:
        print(line[:-1])

def delete_directory(name):
    os.remove(f"directories/{name}.txt")

GREETING = ("Выберите одну из операций:\n"
                "1: создать новый справочник: <1> <Название справочника>\n"
                "2: просмотр всего справочника: <2> <Название справочника>\n"
                "3: создать новую запись: <3> <Название справочника> <Запись>\n"
                "4: найти запись: <4> <Название справочника> <Почта или телефон записи>\n"
                "5: удалить запись: <5> <Название справочника> <Почта или телефон записи>\n"
                "6: изменить запись: <6> <Название справочника> <Почта или телефон записи> <Новая запись>\n"
                "7: удалить справочник: <7> <Название справочника>\n"
                "8: помощь: <8>\n"
                "9: выйти из программы: <9>\n")

def help():
    print(GREETING)

help()
while (True):
    command = input().split()
    if (not command): continue
    if (command[0] == '1' and len(command) == 2):
        create_directory(command[1])
    elif (command[0] == '2' and len(command) == 2):
        read_directory(command[1])
    elif (command[0] == '3' and len(command) == 7):
        create_record(command[1], command[2:7])
    elif (command[0] == '4' and len(command) == 3):
        find_record(command[1], command[2])
    elif (command[0] == '5' and len(command) == 3):
        replace_or_remove_record(command[1], str(command[2]))
    elif (command[0] == '6' and len(command) == 8):
        replace_or_remove_record(command[1], command[2], command[3:8])
    elif (command[0] == '7' and len(command) == 2):
        delete_directory(command[1])
    elif (command[0] == '8'):
        quit()
    elif (command[0] == '9'):
        help()
    else:
        print("Неверный формат команды!")

