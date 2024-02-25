# Створіть прототип програми «Облік кадрів», в якій є можливість перегляду та внесення змін до
# структури(реалізуйте інтерфейс(меню), за допомогою якого можна робити маніпуляції з даними):
#
# прізвище:#
#     посада: ...#
#     досвід роботи: …#
#     портфоліо: …#
#     коефіцієнт ефективності: …#
#     стек технологій: …
##     зарплата: …#
# Передбачте можливість виведення на екран сортування за прізвищем та найефективнішим співробітником

employees_dict = {
    "Petrenko": {
        "position": "manager",
        "experience": 25,
        "portfolio": "portfolio Petrenko",
        "efficiency factor": 80,
        "technology stack": "technology stack Petrenko",
        "salary": 25000
    },
    "Leshkiv": {
        "position": "manager2",
        "experience": 20,
        "portfolio": "portfolio Leshkiv",
        "efficiency factor": 65,
        "technology stack": "technology stack Leshkiv",
        "salary": 15000
    },
    "Petruk": {
        "position": "manager3",
        "experience": 10,
        "portfolio": "portfolio Petruk",
        "efficiency factor": 90,
        "technology stack": "technology stack Petruk",
        "salary": 30000
    }
}

while True:
    print("Виберіть, що необхідно зробити: \n1. список робітників,\n2. додати робітника,\n"
          "3. редагування прізвища робітника,\n4. редагування даних робітника,\n5. видалення\n6. Вихід з програми")
    choose = input("Введіть вибране значення: ")

    if choose == "1":
        for i in employees_dict.items():
            print(i)

    elif choose == "2":
        employee_name = input("Введіть Прізвище: ")
        position = input("Введіть посаду: ")
        experience = input("Введіть досвід роботи: ")
        portfolio = input("Введіть портфоліо: ")
        efficiency_factor = int(input("Введіть коефіцієнт ефективності: "))
        technology_stack = input("Введіть стек технологій: ")
        salary = int(input("Введіть зп: "))

        new_employee_dict = {"position": position,
                             "experience": experience,
                             "portfolio": portfolio,
                             "efficiency factor": efficiency_factor,
                             "technology stack": technology_stack,
                             "salary": salary
                             }

        employees_dict[employee_name] = new_employee_dict

    elif choose == "3":
        for index, employee in enumerate(employees_dict):
            print(f"{index + 1}. {employee}")

        employee_num = int(input("Введіть номер призвіща, яке необхідно змінити: "))
        if employee_num > len(employees_dict):
            print("Ви ввели не вірні дані")
            continue
        employee_name_new = input("Введіть нове призвіще: ")
        employee_name = ""
        for index, employee in enumerate(employees_dict):
            if index == employee_num - 1:
                employee_name = employee
        employees_dict[employee_name_new] = employees_dict.pop(employee_name)

    elif choose == "4":
        for index, employee in enumerate(employees_dict):
            print(f"{index + 1}. {employee}")

        employee_num = int(input("Введіть номер призвіща, в якому необхідно змінити дані: "))
        if employee_num > len(employees_dict):
            print("Ви ввели не вірні дані")
            continue
        employee_name = ""
        for index, employee in enumerate(employees_dict):
            if index == employee_num - 1:
                employee_name = employee
        print(employees_dict.items())
        for index, value in enumerate(employees_dict.get(employee_name)):
            print(f"{index + 1}. {value}")

        employee_data_num = int(input("Введіть номер необхідного параметру, який необхідно змінити: "))
        if employee_data_num > len(employees_dict[employee_name]):
            print("Ви ввели не вірні дані")
            continue
        employee_data_new = input("Введіть нове значення: ")
        employee_data = ""

        for index, value in enumerate(employees_dict.get(employee_name)):
            if index == employee_data_num - 1:
                employee_data = value
                employees_dict[employee_name][employee_data] = employee_data_new
        for i in employees_dict.items():
            print(i)
    elif choose == "5":
        for index, employee in enumerate(employees_dict):
            print(f"{index + 1}. {employee}")

        employee_num = int(input("Введіть номер призвіща якого необхідно видалити: "))
        employee_name = ""
        for index, employee in enumerate(employees_dict):
            if index == employee_num - 1:
                employee_name = employee
        del employees_dict[employee_name]

    elif choose == "6":
        break

    else:
        print("Ви ввели не вірні дані")
