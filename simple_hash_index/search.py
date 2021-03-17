import hashlib

# s - искомое слово
s = "1RwtJd-0009RI-9q"
key = hashlib.md5(s.encode()).hexdigest()

# открываем файл index, ищем совпадение по хэшу
fd = open('index', 'r')
for line in fd:
    word = line.rstrip("\n").split(":")
    if word[0] == key:
        # после того, как нашли нужный хэш, извлекаем номера строк базового файла, где встречается указанное слово
        lines = [ int(i) for i in word[1].split(",") ]

        was_found = 0
        lines_len = len(lines)
        line_number = 1

        # открываем файл out и ищем в нем нужные строки (по номеру строки)
        fd1 = open('out', 'r')
        for line1 in fd1:
            if line_number in lines:
                was_found += 1
                print(line1)

            line_number += 1
            if was_found >= lines_len:
                # мы нашли все перечисленные строки, просматривать файл далее не имеет смысла
                break

        fd1.close()
        break

fd.close()
