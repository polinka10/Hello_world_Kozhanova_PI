volume = float(input("Введите нужный объем раствора (мл): "))
salt_mass = volume * 0.89
water_volume = volume - salt_mass
with open("recipe.txt", "w", encoding="utf-8") as f:
    f.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    f.write("---\n")
    f.write(f"Общий объем: {volume:.2f} мл\n")
    f.write(f"Масса соли: {salt_mass:.2f} г\n")
    f.write(f"Объем воды: {water_volume:.2f} мл\n")
print("Рецепт сохранен в файл recipe.txt")