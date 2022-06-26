import glob


def sort_files_by_lines():
    source_files = glob.glob('*txt')
    count_lines = dict()
    for file in source_files:
        with open(file, 'r', encoding='utf-8') as file_r:
            count_lines[len(file_r.readlines())] = file
    sorted_files = sorted(count_lines.items())
    with open('result_file.txt', 'w', encoding='utf-8') as file_w:
        for name in sorted_files:
            file_w.write(f'{name[1]}\n')
            file_w.write(f'{name[0]}\n')
            data = open(name[1], 'r', encoding='utf-8')
            file_w.write(f'{data.read()}\n')


sort_files_by_lines()
