# Задание 1: добавление даты к именам файлов
files = ["seq1", "seq2.fasta", "seq3.fa", "seq4"]
date = "2025-03-15"

for name in files:
    # Проверяем, заканчивается ли имя на .fasta
    if name.endswith(".fasta"):
        # Убираем расширение .fasta, чтобы добавить дату и снова его приписать
        base = name[:-6]  # удаляем ".fasta"
        new_name = f"{base}_{date}.fasta"
        print(f"{name} уже имел расширение, теперь: {new_name}")
    else:
        # Добавляем дату и расширение .fasta
        new_name = f"{name}_{date}.fasta"
        print(f"{new_name}")