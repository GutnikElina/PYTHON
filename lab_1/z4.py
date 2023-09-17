"""Создайте словарь из строки ' Follow your heart' следующим образом:
в качестве ключей возьмите символы строки, а значениями
пусть будут числа, соответствующие количеству вхождений данноq буквы в строку."""

stroka = 'Follow your heart'
dictionary = {}
print(stroka)
for char in stroka:
    if char.isalpha() or char.isspace():
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
print(dictionary)
