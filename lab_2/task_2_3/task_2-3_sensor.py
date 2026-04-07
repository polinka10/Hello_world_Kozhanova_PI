operator_name = input("Введите имя оператора: ")
pressure_value = input("Введите текущее значение давления (Па): ")

with open("sensor_log.txt", "a", encoding="utf-8") as file:
    file.write(f"Оператор: {operator_name}\n")
    file.write(f"Давление: {pressure_value} Па\n")
    file.write("-" * 20 + "\n")

print("Данные успешно сохранены в sensor_log.txt.")