from math import ceil


def get_chess_board(width, length):

    array, sign = [], -1
    for row in range(length):
        sign = sign * - 1
        if row % 2 == 0:
            a = '* ' * ceil(width/2)
            array.append(a)
        else:
            a = ' *' * (ceil((width + (1 * sign)) / 2))
            array.append(a[:-1])
        print(a)
    print(array)
    return array


def get_validation_row_column():

    while True:
        try:
            number = int(input())
            try:
                if 0 < number <= 100:
                    return number
                else:
                    raise ValueError('Range of numbers is wrong')
            except ValueError:
                print(f'Range of numbers is wrongs. {number} < 0 or > 100. Input correct number, please')
        except ValueError:
            print('It must be digits')


def main():
    print("Input width , please: ")
    width_data = get_validation_row_column()
    print("Input length , please: ")
    length_data = get_validation_row_column()
    get_chess_board(width_data, length_data)

if __name__ == '__main__':
    main()
