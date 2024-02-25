#п.1 Дано два рядки. Виведіть на екран символи, які є в обох рядках.
str1 = input("введіть рядок 1: ")
str2 = input("Введіть рядок 2: ")
set1 = set(str1)
set2 = set(str2)
print(set1.intersection(set2))