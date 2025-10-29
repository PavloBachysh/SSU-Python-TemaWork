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
            SortStudents()
        case 4:
            print("Вивід")
        case 5:
            break


