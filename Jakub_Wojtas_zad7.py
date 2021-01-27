def person_print(name, last_name, *others, age) -> object:
    formatted_data = 'Imię: {}, nazwisko: {}, wiek: {}'.format(name, last_name, age)
    others_str = ' '
    for arg in others:
        others_str += arg + ' '
    print(formatted_data + others_str)

person_print("Jakub", "Wojtas", "Student", "IIrok", age=21)