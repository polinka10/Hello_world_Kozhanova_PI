medium_name = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
sterilization_temp = input("Введите температуру стерилизации: ")

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"Название среды: {medium_name}\n")
    file.write("Параметры:\n")
    file.write(f"  - Концентрация агара: {agar_concentration}%\n")
    file.write(f"  - Температура стерилизации: {sterilization_temp}\n")

print("Данные сохранены в файл recipe.txt")