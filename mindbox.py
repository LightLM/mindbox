def count_(n):qweqwe
    dict_clients = {}
    for i in range(n):
        number_sum = sum(map(int, list(str(i))))
        if number_sum in dict_clients.keys():
            dict_clients[number_sum] += 1
        else:
            dict_clients[number_sum] = 1
    return dict_clients


try:
    number = int(input('Введите кол-во клиентов: '))
    new = count_(number)
    for i in new.items():
        print(f'Сумма цифр в числе: {i[0]} и их кол-во: {i[1]}')
except:
    print('Что то пошло не так(')


def count_2(n, first):
    dict_clients = {}
    for i in range(first, first + n):
        number_sum = sum(map(int, list(str(i))))
        if number_sum in dict_clients.keys():
            dict_clients[number_sum] += 1
        else:
            dict_clients[number_sum] = 1
    return dict_clients


try:
    number = int(input('Введите кол-во клиентов: '))
    first_client = int(input('Введите ID первого клиента: '))
    new = count_2(number, first_client)
    for i in new.items():
        print(f'Сумма цифр в числе: {i[0]} и их кол-во: {i[1]}')
except:
    print('Что то пошло не так(')
