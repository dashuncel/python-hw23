import chardet

def read_file(file_name):
    with open(file_name, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        return data.decode(result['encoding'])


def getKeys(dict, val):
    keys = []
    for key, elem in dict.items():
        if val == elem:
           keys.append(key)
    return keys


def det_frequency(text):
    wordlist = text.lower().split(None)
    print(wordlist)
    frequencies = {}
    for word in wordlist:
        if len(word) < 6:
            continue
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    i = 0
    req = sorted(list(frequencies.values()), reverse=True)
    print('Часто встречающиеся слова в тексте:')
    while i < min(6, len(req)):
        print('{} - {} раз'.format(getKeys(frequencies, req[i]), req[i]))
        i += 1

det_frequency('bllabla blabla BLabla bllabla bllabla assssss assssss assssss assssss assssss')
det_frequency(read_file('newsfr.txt'))
det_frequency(read_file('newsit.txt'))
det_frequency(read_file('newsafr.txt'))

