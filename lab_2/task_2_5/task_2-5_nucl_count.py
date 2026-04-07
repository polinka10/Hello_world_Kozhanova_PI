# Запрашиваем у пользователя последовательность ДНК
dna = input("Введите последовательность ДНК: ")

# Переводим всю строку в верхний регистр (чтобы подсчёт был регистронезависимым)
dna_upper = dna.upper()

# Выводим заголовок анализа
print("=== Анализ последовательности ДНК ===")
print("Последовательность в верхнем регистре:", dna_upper)

# Подсчитываем количество каждого нуклеотида с помощью метода count()
a_count = dna_upper.count('A')
t_count = dna_upper.count('T')
g_count = dna_upper.count('G')
c_count = dna_upper.count('C')

# Определяем длину последовательности
length = len(dna_upper)

# Выводим результаты подсчёта
print("Подсчёт нуклеотидов:")
print(f"A: {a_count}")
print(f"T: {t_count}")
print(f"G: {g_count}")
print(f"C: {c_count}")

# Выводим общую длину
print(f"\nОбщая длина: {length} нуклеотидов")

# Если последовательность не пустая, считаем и выводим проценты
if length > 0:
    print("\nПроцентное содержание:")
    print(f"A: {a_count / length * 100:.1f}%")
    print(f"T: {t_count / length * 100:.1f}%")
    print(f"G: {g_count / length * 100:.1f}%")
    print(f"C: {c_count / length * 100:.1f}%")