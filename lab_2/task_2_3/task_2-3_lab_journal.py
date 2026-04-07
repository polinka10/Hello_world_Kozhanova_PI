name = input("Введите ФИО исследователя: ")
date = input("Введите дату: ")
experiment = input("Введите название эксперимента: ")
conclusion = input("Введите вывод: ")

width = 50
top = "+" + "-" * width + "+\n"
header = "| Электронный лабораторный журнал" + " " * (width - len("| Электронный лабораторный журнал")) + "|\n"
separator = "+" + "-" * width + "+\n"
name_line = f"| ФИО исследователя : {name}" + " " * (width - len(f"| ФИО исследователя : {name}")) + "|\n"
date_line = f"| Дата : {date}" + " " * (width - len(f"| Дата : {date}")) + "|\n"
exp_line = f"| Эксперимент : {experiment}" + " " * (width - len(f"| Эксперимент : {experiment}")) + "|\n"
separator2 = "+" + "-" * width + "+\n"
conclusion_header = "| Вывод:" + " " * (width - len("| Вывод:")) + "|\n"

if len(conclusion) <= width - 2:
    conclusion_line = f"| {conclusion}" + " " * (width - len(f"| {conclusion}")) + "|\n"
else:
    conclusion = conclusion[:width-5] + "..."
    conclusion_line = f"| {conclusion}" + " " * (width - len(f"| {conclusion}")) + "|\n"

bottom = "+" + "-" * width + "+\n"

with open("journal.txt", "w", encoding="utf-8") as f:
    f.write(top)
    f.write(header)
    f.write(separator)
    f.write(name_line)
    f.write(date_line)
    f.write(exp_line)
    f.write(separator2)
    f.write(conclusion_header)
    f.write(conclusion_line)
    f.write(bottom)

print("Данные успешно сохранены в файл journal.txt")