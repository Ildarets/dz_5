import json
import os
from decorator import add_separators, my_bill, add_sep2


@add_separators
def my_bank_account():
    bill_list = []
    spending = {}
    bill_dig = 0

    FILE_NAME = 'bill.json'
    FILE_SPENDING = 'spending.json'
    BILL = 'bill_dig.json'

    if os.path.exists(FILE_NAME):
        with open (FILE_NAME, 'r') as f:
            bill_list = json.load(f)

    if os.path.exists(FILE_SPENDING):
        with open (FILE_SPENDING, 'r') as f:
            spending = json.load(f)

    if os.path.exists(BILL):
        with open (BILL, 'r') as f:
            bill_dig = json.load(f)

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. история пополнений')
        print('5. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            money = int(input("Введите сумму пополнения: "))
            bill_list.append(money)
            bill_dig += money
            continue

        elif choice == '2':
            purchase = int(input("Введите сумму покупки: "))
            if bill_dig >= purchase:
                name__purchase = input("Введите название покупки: ")
                spending[name__purchase] = purchase
                bill_dig -= purchase
                continue
            else:
                print("Денег не хватает!")
                continue

        elif choice == '3':
            for key, value in spending.items():
                print(key, value)
            continue

        elif choice == '4':
            my_bill(bill_list)
            continue

        elif choice == '5':
            with open(FILE_NAME, 'w') as f:
                json.dump(bill_list,f)

            with open(FILE_SPENDING, 'w') as f:
                json.dump(spending, f)

            # на случай если денег не хватает. Считает количесво денег в кошельке.
            with open(BILL, 'w') as f:
                json.dump(bill_dig, f)

            break
        else:
            print('Неверный пункт меню!')