import glob

def split_sort_files():
    a = {}
    for filename in glob.glob('*txt'):
        with open(filename, 'rt', encoding='utf-8') as f:
            stroki = len(f.readlines())
        with open(filename, 'rt', encoding='utf-8') as f:
            a[filename] = [stroki, f.read().strip()]
    # from operator import itemgetter
    # a = sorted(a.items(), key=itemgetter(1))
    with open('result.txt', 'a', encoding='utf-8') as result_file:
        a = sorted(a.items(), key=lambda x: x[1])
        for i in a:
            result_file.write(i[0] + '\n')
            for j in i[1]:
                result_file.write(str(j) + '\n')
    print(f'Обработка файлов завершена!')

split_sort_files()