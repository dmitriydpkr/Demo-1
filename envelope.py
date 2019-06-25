def check_envelope_size(width_1, length_1, width_2, length_2):

    if (width_1 - width_2 > 0 and length_1 - length_2 > 0) or (width_1 - length_2 > 0 and length_1 - width_2) > 0:
        return 'The envelope fits '
    else:
        return "The envelop don't fit "


def get_validation_data():

    while True:
        try:
            input_data = float(input())
            try:
                if 0 < input_data <= 1000000:
                    return float(input_data)
                else:
                    print('ValueError')
            except UnboundLocalError:
                print('UnboundLocalError')

        except ValueError:
            print('It must be digits')


def main():
    question = 'yes'
    while question == 'yes' or question == 'y':
        print("Input width the first Envelope, please: ")
        width_envelope1 = get_validation_data()
        print("Input length the first Envelope, please: ")
        length_envelope1 = get_validation_data()
        print("Input width the second Envelope, please: ")
        width_envelope2 = get_validation_data()
        print("Input length the first Envelope, please: ")
        length_envelope2 = get_validation_data()
        print(check_envelope_size(width_envelope1, length_envelope1, width_envelope2, length_envelope2))
        question = input("Do yo want continue  yes / y ? ")

if __name__ == '__main__':
    main()
