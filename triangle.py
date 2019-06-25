from math import sqrt

array_key = []
array_value = []


def triangles():

    count = 0
    question = 'y'
    while question == 'y' or question == 'yes':

        line_arg = get_lines_arguments()
        name_triangle = line_arg[0]
        side_1 = line_arg[1]
        side_2 = line_arg[2]
        side_3 = line_arg[3]

        half_perimeter = (side_1 + side_2 + side_3) / 2
        square = round(sqrt(half_perimeter * (half_perimeter - side_1) * (half_perimeter - side_2) *
                            (half_perimeter - side_3)), 3)

        array_key.append(name_triangle)
        array_value.append(square)

        question = input("Add new triangle for rating  yes / y ? ")

    array_kv = dict(zip(array_key, array_value))
    sorted_array = sorted(array_kv.items(), reverse=True, key=lambda kv: kv[1])
    for item in sorted_array:
        count += 1
        print(f'{count}. Triangle [{item[0]}]: {item[1]} cm')

    return sorted_array


def get_lines_arguments():

    def main():
        arguments = []
        request = input('Введите условия согласно формата:''<имя>, <длина стороны>, <длина стороны>, '
                        '<длина стороны>: ').strip()
        if request.count(',') < 3:
            main()
        else:
            line = request.split(',')
            name_tr = validation_data_str(line[0])
            len1 = test_sides(line[1])
            len2 = test_sides(line[2])
            len3 = test_sides(line[3])

            if (not len1 < (len2 + len3) or not len1 > (len2 - len3)) and \
                (not len2 < (len1 + len3) or not len2 > (len1 - len3)) and \
                    (not len3 < (len1 + len2) or not len3 > (len1 - len2)):
                print("The sides of triangle don't have correct length. Try again, please. ")
                get_lines_arguments()
            else:
                arguments.append(name_tr)
                arguments.append(len1)
                arguments.append(len2)
                arguments.append(len3)

                return arguments

    def test_sides(side):

        try:
            if not float(side):
                print(f"The side number  is wrong, please, input again correct data")
        except ValueError:
            print(f'It must be only digits. One side is wrong ')
            main()

        if not 0 < float(side) <= 10 ** 8:
            print(f"The side is not in allowed size, please, input again correct data")
            main()
        else:
            return float(side)

    def validation_data_str(name):

        try:
            if 0 <= len(name) <= 50:
                return name
            else:
                print('Character limit exceeded.')
                main()
        except UnboundLocalError:
            print('Character limit exceeded')

    return main()


if __name__ == '__main__':
    triangles()

