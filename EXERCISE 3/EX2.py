import MapReduce

mr = MapReduce.MapReduce()


def mapper(record):
    type = record[0]
    order_id = record[1]
    data = record[2:]
    mr.emit_intermediate(order_id, (type, data))


def reducer(key, values):
    order_type, data_temp = values[0]
    order = [order_type, key] + data_temp
    for type, data in values[1:]:
        order = order + [type, key] + data
        mr.emit(order)
        order = [order_type, key] + data_temp


if __name__ == '__main__':
    inputdata = open(".\\Data\\records.json")
    mr.execute(inputdata, mapper, reducer)
