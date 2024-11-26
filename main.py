def input_strings():
    strings = []
    print("Введите строки (введите 'end' для завершения ввода):")
    while True:
        string = input()
        if string.lower() == 'end':
            break
        strings.append(string)
    return strings
strings = input_strings()
