import random

#  /media/ukrainer/G/Methods.txt


def define_mode():

    modes = []
    while len(modes) < 1:
        try:
            source_file_mode = input('Input path to file with define method, please: ').strip()
            file_mode = open(source_file_mode, mode='r', encoding='utf8')
            for line in file_mode:
                modes.append(line.strip().lower())
            file_mode.close()
            return modes
        except IOError:
            print('Not correct path for file. Please, input again.')


def get_number_tickets():

    while True:
        try:
            get_number = int(input("Input amount of tickets for method: "))
            try:
                if 0 < get_number <= 10 ** 8:
                    return get_number
                else:
                    print('ValueError')
            except UnboundLocalError:
                print('UnboundLocalError')
        except ValueError:
            print('It must be digits')


numbers = [str(random.randint(000000, 999999)) for i in range(get_number_tickets())]


def method_moscow():

    moscow_tickets = 0
    for number in numbers:
        first_half = [int(n) for n in str(number)[:3]]
        second_half = [int(n) for n in str(number)[3:]]

        if sum(first_half) == sum(second_half):
            moscow_tickets += 1
    return f'Moscow tickets = {moscow_tickets}'


def method_piter():

    piter_tickets = 0
    for number in numbers:
        even, odd = 0, 0
        for char in numbers:
            if int(number) % 2 == 0:
                even += int(char)
            else:
                odd += int(char)
        if even == odd:
            piter_tickets += 1
    return f'Piter tickets = {piter_tickets}'


def main():
    modes = define_mode()
    if modes[0] == 'Moscow' and modes[1] == 0:
        print(method_moscow())
    elif modes[0] == 'Piter' and modes[1] == 0:
        print(method_piter())
    else:
        print(method_moscow())
        print(method_piter())

if __name__ == '__main__':
    main()




