import MapReduce


mr = MapReduce.MapReduce()


def mapper(record):
    person = record[0]
    mr.emit_intermediate(person, 1)


def reducer(key, values):
    person = key
    total = sum(values)
    mr.emit((person, total))


if __name__ == '__main__':
    inputdata = open(".\\Data\\friends.json")
    mr.execute(inputdata, mapper, reducer)
