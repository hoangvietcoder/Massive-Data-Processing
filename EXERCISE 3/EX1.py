import MapReduce

mr = MapReduce.MapReduce()


def mapper(record):
    value = record[1]
    words = value.split()
    for word in words:
        mr.emit_intermediate(word, 1)


def reducer(key, values):
    total = 0
    for value in values:
        total += value
    mr.emit((key, total))


if __name__ == '__main__':
    inputdata = open(".\\Data\\data.json")
    mr.execute(inputdata, mapper, reducer)
