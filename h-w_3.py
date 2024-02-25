# п.3 Створіть програму, яка має 2 списки цілочисельних значень та друкує список унікальних значень
# без повтору, які є в 1 списку (немає в другому) і навпаки.

while True:
    print("Для виходу зі списку введіть s")
    str1 = input("введіть цілі числа через кому для формування списку1: ")
    if str1 == "s":
        break
    list1 = str1.split(",")
    is_correct = True
    for i in list1:
        if i.isdigit() == False:
            print("Ви ввели не число або не ціле число для списку1")
            is_correct = False
            break

    if is_correct == False:
        continue
    list1_int = [int(i) for i in list1]

    print("Для виходу зі списку введіть s")
    str2 = input("введіть цілі числа через кому для формування списку2: ")
    if str1 == "s":
        break
    list2 = str2.split(",")

    for i in list2:
        if i.isdigit() == False:
            print("Ви ввели не число або не ціле число для списку2")
            is_correct = False
            break
    if is_correct == False:
        continue

    list2_int = [int(i) for i in list2]
    set1 = set(list1_int)
    set2 = set(list2_int)
    print(f"Унікальні значення першого списку: {set1.difference(set2)}, "
          f"унікальні значення другого списку: {set2.difference(set1)}")