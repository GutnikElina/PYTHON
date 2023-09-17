"""Дана строка, в которой имеется текст в скобках. Удалить частьтекста, заключенного в скобки. """

stroka = "Номер телефона (+375291234567)"
print("ТЕКУЩАЯ СТРОКА:  ", stroka)
new_stroka = ""
in_brackets = False
for char in stroka:
    if char == '(':        in_brackets = True
    elif char == ')':        in_brackets = False
    elif not in_brackets:        new_stroka += char
print("ПОСЛЕ УДАЛЕНИЯ ТЕКСТА В СКОБКАХ:  ", new_stroka)
