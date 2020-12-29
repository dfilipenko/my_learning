# До прочтения про pep8 пока не дошли руки, обязательно прочитаю на каникулах

with open ('fitst_file.txt', 'w') as f_obj:     #First exercise
    data_list = input('Введите данные')
    while True:
        f_obj.write(data_list + '\n')
        data_list = input('Введите данные')
        if data_list == "":
            break

with open ('second_file.txt', 'r') as f_obj:      #Second exercise
    number = 0
    for item in f_obj:
        list = item.split()
        print (f"В {number+1} строке {len(list)} слов")
        number += 1
    print('Всего строк в документе:', number)

with open ('third_file.txt', 'r', encoding='utf-8') as f_obj:      #Third exercise
    income = []
    for item in f_obj:
        list = item.split(' - ')
        income.append(list[1])
        if int(list[1]) < 20000:
            print (' - '.join(list))
    middle = (sum(map(int, income))) / len(income)
    print(middle)

