import MapReduce

mr = MapReduce.MapReduce()


def mapper(record):
    matrix = record[0]
    row, col = record[1:3]
    value = record[3]
    for i in range(5):
        if matrix == 'a':
            mr.emit_intermediate((row, i), (col, matrix, value))
        else:
            mr.emit_intermediate((i, col), (row, matrix, value))


def reducer(key, values):
    values.sort()
    total = 0
    for i in range(len(values) - 1):
        if values[i][0] == values[i + 1][0]:
            total += values[i][2] * values[i + 1][2]

    mr.emit((key[0], key[1], total))


if __name__ == '__main__':
    inputdata = open(".\\Data\\matrix.json")
    mr.execute(inputdata, mapper, reducer)
