import memory_profiler as mem_profile
import time
import argparse


def create_fibo_range(number_min, number_max):
    ar_min_fibo, ar_result = [], []
    counter = 0

    def definite_start(f_start):
        fibo1, fibo2 = 0, 1
        for i in range(f_start):
            fibo1, fibo2 = fibo2, fibo1 + fibo2
            yield fibo1

    def definite_finish(f_finish):
        fib1, fib2 = f1, f2
        for number in range(f_finish):
            fib1, fib2 = fib2, fib1 + fib2
            yield fib1

    if number_min < 2:
        for element in definite_start(number_max):
            ar_result.append(element)
    else:
        for element in definite_start(number_min):
            counter += 1
            if counter > number_min - 2:
                ar_min_fibo.append(element)

        f1, f2 = ar_min_fibo[0], ar_min_fibo[1]
        for element in definite_finish(number_max - number_min + 1):
            ar_result.append(element)

    return ar_result


def get_validate_arguments(f_min, f_max):
    if f_min < 0 or f_max <= f_min or f_max - f_min == 0:
        raise ValueError('Range of numbers is wrong')
    else:
        return True


def main_arg():
    parser = argparse.ArgumentParser(description='Calculate numbers Fibonacci')
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", help="Output data in order ", action="store_true")
    parser.add_argument('number_min', type=int, help="The Fibonacci start number you wish to calculate.")
    parser.add_argument('number_max', type=int, help="The Fibonacci finish number you wish to calculate.")
    parser.add_argument("-o", "--output", help="Output the result to a file", action="store_true")
    args = parser.parse_args()
    result = 0
    if get_validate_arguments(args.number_min, args.number_max):
        result = create_fibo_range(args.number_min, args.number_max)

    if args.verbose:
        t1 = time.clock()
        memory_1 = mem_profile.memory_usage()
        for count, item in enumerate(result, 1):
            print(f'{count}. {item}')
        memory_2 = mem_profile.memory_usage()
        t2 = time.clock()
        print('Memory (Before): ' + str(memory_1) + 'MB'), print('Memory (After) : ' + str(memory_2) + 'MB')
        print('It took ' + str(round(t2 - t1, 3)) + ' Seconds')
    elif args.output:
        f = open("fibonacci.txt", "w")
        for n, value in enumerate(result, 1):
            f.write(str(n) + ". " + str(value) + "\n")
        f.close()
    else:
        print(result)


if __name__ == '__main__':
    main_arg()



