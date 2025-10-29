#Додавання студенту в список - Бачиш Павло  DONE
#Видалення студента з списку - Борзаниця Олександр
#Сортування - Грінченко Дмитро
#Вивід - Сагайдак Богдан

#Список з усіма студентами
allStudents = []


#Функція додавання нового студента в список
def AddStudent():
    try:
        group = str(input("Введіть групу студента: "))
        pib = str(input("Введіть ПІБ студента: "))
        course = int(input("Введіть номер курсу студента (числом): "))
    except:
        print("Некоректно введені дані")
        return

    sub = []
    mark = []

    while(True):
        s = str(input("Введіть назву предмету (Щоб закінчити ввод предметів і оцінок - введіть STOP): "))
        if (s == "STOP"):
            break
        while (True):
            try:
                m = int(input(f"Введіть оцінку предмета {s} (числом): "))
                break
            except:
                print("Некоректно введені дані")
                continue

        sub.append(s)
        mark.append(m)

    subjects = dict(zip(sub, mark))

    student = {
    "Group": group,
    "PIB": pib,
    "Course": course,
    "Subjects": subjects
    }


    #Чи є такий студент вже в списку
    for st in allStudents:
        if(st.get("PIB") == pib):
            print(
                "Такий студент вже є у списку\n",
                "1 - Це інший студент, внести його в список",
                "\n2 - Змінити дані студента"
                )
            try:
                funcNum = int(input("Оберіть одну з запропонованих функцій: "))
            except:
                print("Некоректно введені дані")
                return
            match funcNum:
                case 1:
                    allStudents.append(student)
                    return
                case 2:
                    allStudents[allStudents.index(st)] = student
                    return

    allStudents.append(student)

#Фунція друку даних
def out ():
    while True:
        print(
            "1 - вивести дані усіх студентів",
            "\n2 - вивести дані одного студента"
            )
        try:
            check = int(input("Оберіть одну з запропонованих функцій: "))
        except:
            print("Некоректно введені дані")
            continue
        if check != 1 and check!=2:
            continue
        break

    match check:
        case 1:
            if not allStudents:
                print("Список студентів порожній.")
                return

            for st in allStudents:
                print(f"\n====================")
                print(f"ПІБ: {st['PIB']}")
                print(f"Група: {st['Group']}")
                print(f"Курс: {st['Course']}")
                print("Предмети та оцінки:")
                for subj, mark in st["Subjects"].items():
                    print(f"  - {subj}: {mark}")

        case 2:
            search_pib = input("Введіть ПІБ студента: ")
            found = 0
            for st in allStudents:
                if st["PIB"] == search_pib:
                    print("\n=== Інформація про студента ===")
                    print(f"ПІБ: {st['PIB']}")
                    print(f"Група: {st['Group']}")
                    print(f"Курс: {st['Course']}")
                    print("Предмети та оцінки:")
                    for subj, mark in st["Subjects"].items():
                        print(f"  - {subj}: {mark}")
                    found += 1

            if not found:
                print("\nСтудента з таким ПІБ не знайдено.")

# Функція сортування студентів за обраним критерієм
def SortStudents():
    # Перевірка чи є студенти для сортування
    if len(allStudents) == 0:
        print("Список студентів порожній")
        return

    # Вибір критерію сортування
    print("\nКритерії сортування:")
    print("1 - За групою")
    print("2 - За ПІБ")
    print("3 - За курсом")
    print("0 - Закінчити сортування")

    try:
        sortChoice = int(input("Оберіть критерій сортування: "))
    except:
        print("Некоректно введені дані")
        return

    if sortChoice == 0:
        return

    # Вибір порядку сортування
    print("\nПорядок сортування:")
    print("1 - За зростанням (від А до Я, від меншого до більшого)")
    print("2 - За спаданням (від Я до А, від більшого до меншого)")

    try:
        orderChoice = int(input("Оберіть порядок сортування: "))
    except:
        print("Некоректно введені дані")
        return

    if orderChoice == 2:
        reverseOrder = True
    else:
        reverseOrder = False


    # Сортування словнику за обраним критерієм
    match sortChoice:
        case 1:
            # Сортування за групою
            allStudents.sort(key=lambda student: student["Group"], reverse=reverseOrder)

        case 2:
            # Сортування за ПІБ
            allStudents.sort(key=lambda student: student["PIB"], reverse=reverseOrder)

        case 3:
            # Сортування за курсом
            allStudents.sort(key=lambda student: student["Course"], reverse=reverseOrder)

        case _:
            print("Некоректний вибір критерію сортування.Вихід з сортування")
            return

    print("Словник успішно відсортовано")
#Сам функціонал програми
while(True):
    print(
        "1 - Додавання студента",
        "\n2 - Видалення студента",
        "\n3 - Сортування",
        "\n4 - Вивести список стдентів"
        "\n5 - Завершити програму",
    )
    try:
        funcNum = int(input("Оберіть одну з запропонованих функцій: "))
    except:
        print("Некоректно введені дані")
        break
    match funcNum:
        case 1:
            AddStudent()
        case 2:
            print("Видалення")
        case 3:
            print("Сортування")
            SortStudents()
        case 4:
            print("Вивід")
            out()
        case 5:
            break

