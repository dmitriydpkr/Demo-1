dic = {
    '0': ['ноль', 'десять', '', '', '', 'десять тысяч', ''],
    '1': ['один', 'одиннадцать', '', 'сто', 'одна тысяча', 'одиннадцать тысяч', ''],
    '2': ['два', 'двенадцать', 'двадцать', 'двести', 'две тысячи', 'двенадцать тысяч', 'двадцать тысяч'],
    '3': ['три', 'тринадцать', 'тридцать', 'триста', 'три тысячи', 'тринадцать тысяч', 'тридцать тысяч'],
    '4': ['четыре', 'четырнадцать', 'сорок', 'четыреста', 'четыре тысячи', 'четырнадцать тысяч', 'сорок тысяч'],
    '5': ['пять', 'пятнадцать', 'пятьдесят', 'пятьсот', 'пять тысяч', 'пятнадцать тысяч', 'пятьдесят тысяч'],
    '6': ['шесть', 'шестнадцать', 'шестьдесят', 'шестьсот', 'шесть тысяч', 'шестнадцать тысяч', 'шестьдесят тысяч'],
    '7': ['семь', 'семнадцать', 'семьдесят', 'семьсот', 'семь тысяч', 'семнадцать тысяч', 'семьдесят тысяч'],
    '8': ['восемь', 'восемнадцать', 'восемьдесят', 'восемьсот', 'восемь тысяч', 'восемнадцать тысяч',
          'восемьдесят тысяч'],
    '9': ['девять', 'девятнадцать', 'девяносто', 'девятьсот', 'девять тысяч', 'девятнадцать тысяч',
          'девяносто тысяч']
}


def get_one_number(num):
    return dic[num][0]


def get_two_numbers(num):
    if num[0] == '1':
        return dic[num[1]][1]
    else:
        return dic[num[0]][2] + " " + dic[num[1]][0]


def get_thee_numbers(num):
    return dic[num[0]][3] + " " + get_two_numbers(num[1:])


def get_four_numbers(num):
    return dic[num[0]][4] + " " + get_thee_numbers(num[1:])


def get_five_numbers(num):
    if num[0] == '1':
        return dic[num[1]][5] + " " + get_thee_numbers(num[2:])
    elif num[1] == '0':
        return dic[num[0]][6] + " " + get_four_numbers(num[1:])
    else:
        return dic[num[0]][2] + " " + get_four_numbers(num[1:])


def output_six_numbers(num):
    return dic[num[0]][3] + " " + get_five_numbers(num[1:])


def input_validation():
    while True:
        try:
            num = int(input('Please input a number: '))
            try:
                if 0 <= num <= 999999:
                    return num
                else:
                    print('ValueError')
            except UnboundLocalError:
                print('UnboundLocalError')

        except ValueError:
            print('It must be only digits')


def main():
    number_to_output = str(input_validation()).zfill(6)
    print(output_six_numbers(number_to_output).strip())


if __name__ == '__main__':
    main()
