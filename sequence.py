def square():
    border = get_number()
    array_square = []
    for i in [x*x for x in range(border)]:
        array_square.append(i)
        return array_square


def get_number():

    while True:
        try:
            number = int(input("Input number, please: "))
            try:
                if 0 <= number <= 10 ** 8:
                    return number
                else:
                    print('ValueError')
            except UnboundLocalError:
                print('UnboundLocalError')
        except ValueError:
            print('It must be digits and integer')

if __name__ == '__main__':
    print(square())

