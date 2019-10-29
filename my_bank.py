def my_bank_account():
    bill_list = []
    spending = {}
    bill_dig = 0


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
            print(*bill_list)
            continue

        elif choice == '5':
            break
        else:
            print('Неверный пункт меню!')