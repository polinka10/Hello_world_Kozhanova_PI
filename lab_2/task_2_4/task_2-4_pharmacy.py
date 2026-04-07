total_capsules = int(input("Введите общее количество произведенных капсул: "))
pack_size = int(input("Введите вместимость одной упаковки: "))
full_packs = total_capsules // pack_size
remaining = total_capsules % pack_size
print(f"Полных упаковок: {full_packs}")
print(f"Остаток капсул: {remaining}")