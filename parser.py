import os


def define_mode():
    modes = []
    while len(modes) < 1:
        try:
            source_file_mode = input("Input path to file with define modes, please. Or input 'exit' "
                                     "to choose mode without file. ").strip()
            if source_file_mode == 'exit':
                modes = input_data_without_file()
            else:
                file_mode = open(source_file_mode, mode='r', encoding='utf8')
                for line in file_mode:
                    modes.append(line.strip().lower())
                file_mode.close()
            return modes
        except IOError:
            print('Not correct path for file. Please, input again.')


def input_data_without_file():

    modes = []
    mode_to_run = input("Input mode, please: (Replace / Occurrence) ")
    if mode_to_run.lower() == 'occurrence' or mode_to_run.lower() == 'replace':
        modes.append(mode_to_run)
        return modes


def validation_file_for_open():

    file = False
    while not file:
        source_file = input().strip()
        try:
            file_open = open(source_file, mode='r', encoding='utf8')
            file_open.close()
            file = True
            return source_file
        except IOError:
            print('Not correct path for file. Please, input again.')


def validation_file_for_write():

    source_store = input().strip()
    if source_store.count('/') > 0:
        file_output = open(source_store, mode='w', encoding='utf8')
        file_output.write("Hallo world")
        file_output.close()
        os.remove(str(source_store))
        return source_store
    else:
        print("Not correct path for file. Please, input again.")
        validation_file_for_write()


def validation_data_str():

    data = False
    while not data:
        valid_data = input()
        try:
            if 0 <= len(valid_data) <= 15:
                data = True
                return valid_data
            else:
                print('Character limit exceeded.')
        except UnboundLocalError:
            print('Character limit exceeded')


def replace_text_infile():

    print('Input path to file for search data, please: ')
    source_file = validation_file_for_open()
    file_input = open(source_file, mode='r', encoding='utf8')
    text = file_input.read()
    file_input.close()

    print('Input path to file for store changed data, please: ')
    source_output = validation_file_for_write()
    file_output = open(source_output, mode='w', encoding='utf8')

    print('Input data to search, please: ')
    search = validation_data_str()

    print('Input data to replace, please: ')
    replace = validation_data_str()

    text = text.replace(search, replace)
    file_output.write(text)
    file_output.close()

    print(f'The file with changed data is saved in {source_output}')
    return f'The file with changed data is saved in {source_output}'


def count_text_occurrence():
    print('Input path to file for search data, please: ')
    source_file = validation_file_for_open()
    text = validation_data_str()

    array_lines = []
    file_open = open(source_file, mode='r', encoding='utf8')
    for row in file_open:
        row_free = row.strip()
        array_lines.append(row_free)
    file_open.close()
    text_array = ''.join(array_lines)

    count_symbols = text_array.count(text)
    if count_symbols == 0:
        count_symbols = 0
    print(f'Count of text occurrence : {count_symbols}')
    return f'Count of text occurrence :{count_symbols}'


def main():
    modes = define_mode()

    if modes[0] == 'occurrence':
        count_text_occurrence()

    elif modes[0] == 'replace':
        replace_text_infile()


if __name__ == '__main__':
    main()
