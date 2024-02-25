# п.6 Створіть прототип програми «Бібліотека», де є можливість перегляду та внесення змін за структурою:
# автор: твір. Передбачте можливість виведення на екран сортування за автором та твором.

list1 = []

dict1 = {
    "William Shakespeare": ["Venus and Adonis", "The Rape of Lucrece", "Romeo and Juliet"],
    "Omar Khayyam": ["The Rubaiyat", "Come fill the cup", "For some we loved"],
    "Honoré de Balzac": ["Eugénie Grandet", "Old Father Goriot", "Lost Illusions", "The Girl with the Golden Eyes",
                         "Hour of my Life"]
}

while True:
    list1 = []
    choose = input(
        "Для виведення на екран введіть 1, для того щоб добавити автора або книгу натисніть 2, видалити 3, сортувати 4 : ")
    if choose == "1":
        count = 0
        for autor, book in dict1.items():
            count += 1
            if book:
                str1 = ", ".join(book)
            else:
                str1 = 'no books'

            print(f"{count}. {autor}: {str1}")
        print("*" * 33)


    elif choose == "2":
        correct = input("Якщо хочете добавити автора, натисніть 1,  книгу 2: ")
        if correct == "1":
            autor_add = input("Введіть автора: ")
            dict1.setdefault(autor_add, [])

        if correct == "2":

            for autor in dict1:
                list1.append(autor)

            for index, value in enumerate(list1):
                print(f"{index + 1}. {value}")

            autor_number = int(input(" введіть номер автора до якого хочете добавити книгу: "))
            autor_value = list1[autor_number - 1]
            books_add = input("Введіть назву книги: ")
            dict1[autor_value] = dict1.get(autor_value, []) + [books_add]

    elif choose == "3":
        correct = input("Якщо хочете видалити автора з книгами, натисніть 1,  книгу 2: ")
        if correct == "1":
            for autor in dict1:
                list1.append(autor)

            for index, value in enumerate(list1):
                print(f"{index + 1}. {value}")

            autor_number = int(input("введіть номер автора якого хочете видалити: "))

            autor_value = list1[autor_number - 1]
            del dict1[autor_value]

        if correct == "2":
            for autor in dict1:
                list1.append(autor)

            for index, value in enumerate(list1):
                print(f"{index + 1}. {value}")

            autor_number = int(input("введіть номер автора книгу якого хочете видалити: "))
            autor_value = list1[autor_number - 1]
            book_list = dict1.get(autor_value)
            for i, value in enumerate(book_list):
                print(f"{i + 1}. {value}")
            book_number = input("Введіть номер книги: ")
            book_number = int(book_number)
            book_list.pop(book_number - 1)
            dict1[autor_value] = book_list

    elif choose == "4":
            sort_autor = sorted(dict1.items())
            for i, value in sort_autor:
                sort_book = sorted(value)
                print(f" {i} : {sort_book}")





