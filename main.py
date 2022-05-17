import csv

path1 = 'resources/numbers.txt'
path2 = 'resources/numbers2.txt'


def gen_sql(a, b):

    data1 = []
    data2 = []

    with open(a, 'r') as f:
        for row in csv.reader(f):
            data1.append(row[0])
        # print(data1)

    with open(b, 'r') as f:
        for row in csv.reader(f):
            data2.append(row[0])
        # print(data2)

    out1 = open('resources/output1.txt', 'w')
    for num in data1:
        out1.writelines(f'INSERT INTO tableName(NUM)\nVALUES({num});\n')
    out1.close()

    out2 = open('resources/output2.txt', 'w')
    for num in data2:
        out2.writelines(f'INSERT INTO tableName(NUM)\nVALUES({num});\n')
    out2.close()


if __name__ == '__main__':
    gen_sql(path1, path2)
