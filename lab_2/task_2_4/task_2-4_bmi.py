weight = float(input("Введите ваш вес (кг): "))
height_cm = float(input("Введите ваш рост (см): "))
height_m = height_cm / 100
bmi = weight / (height_m ** 2)
print("\t--- Отчет о состоянии здоровья ---")
print(f"\tРост: {height_cm} см")
print(f"\tВес: {weight} кг")
print(f"\tИндекс массы тела: {bmi:.2f}")