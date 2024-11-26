def input_strings():
    strings = []
    print("Введите строки (введите 'end' для завершения ввода):")
    while True:
        string = input()
        if string.lower() == 'end':
            break
        strings.append(string)
    return strings

def filter_short_strings(strings):
    short_strings = []
    for string in strings:
        if len(string) <= 3:
            short_strings.append(string)
    return short_strings

