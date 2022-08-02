
def delete_duplicate(name):
    res = ''
    for i in name:
        if i not in res:
            res += i
    return res


def add_files(filenames: list) -> list:
    res = []
    names = []
    extensions = []
    for filename in filenames:
        names.append(delete_duplicate(filename.split('.')[0]))
        extensions.append(filename.split('.')[1])

    max_len = len(max(names))

    for i in range(len(names)):
        name = names[i] + '_' * (max_len - len(names[i]))
        res.append(f'{name}.{extensions[i]}')
    return res

