# app_v1.py
kolichestvo = 0

while True:
    print("\n=== Учёт книг (v1) ===")
    print("1 — Выдать книгу")
    print("2 — Показать количество выданных книг")
    print("3 — Сбросить счётчик")
    print("0 — Выход")

    komanda = input("Введите команду: ")

    if komanda == "1":
        kolichestvo += 1
        print("Книга выдана")
    elif komanda == "2":
        print("Выдано книг:", kolichestvo)
    elif komanda == "3":
        kolichestvo = 0
        print("Счётчик сброшен")
    elif komanda == "0":
        print("Выход из программы")
        break
    else:
        print("Неизвестная команда")
