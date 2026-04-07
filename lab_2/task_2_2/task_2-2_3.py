# Задание 3 - Очистка строки от пробелов
user_input = input("Введите что-нибудь с пробелами в начале и конце: ")
clean_input = user_input.strip()

print("Было введено (с пробелами):", repr(user_input))  # repr показывает скрытые символы
print("После strip():", repr(clean_input))
print("Длина исходной строки:", len(user_input))
print("Длина очищенной строки:", len(clean_input))