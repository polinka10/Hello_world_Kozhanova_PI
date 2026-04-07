proteins = float(input("Введите массу белков (г): "))
fats = float(input("Введите массу жиров (г): "))
carbs = float(input("Введите массу углеводов (г): "))
calories = proteins * 9 + fats * 4 + carbs * 4
print(f"Калорийность продукта: {calories} ккал")