import hashlib


def my_iter(file_path):
    with open(file_path) as f:
        for line in f:
            h = hashlib.md5(line.encode('utf-8'))
            yield h.hexdigest()


for item in my_iter('C:\\Users\\semen\\Documents\\GitHub\\itergen\\result_countries.txt'):
    print(item)
