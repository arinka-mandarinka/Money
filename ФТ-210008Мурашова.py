# Ввод числа пользователем.
def input_num(text):
    while True:
        try:
            num = int(input(text))
        except:
            print('Неверно введенно число. Попробуйте ещё раз!')
            continue

        if num <= 0:
            print(f'Число должно быть больше нуля. Попробуйте ещё раз!')
            continue

        return num

sum = input_num('Введите сумму: ')
# Проходимся по всем номиналам.
for bank in (64, 32, 16, 8, 4, 2, 1):
    if bank > sum:
        continue
    
    # Количество купюр.
    amount = sum // bank 
    # Уменьшаем сумму на найденное количество.
    sum -= amount * bank
    print(f'Количество купюр номиналом {bank}: {amount}')