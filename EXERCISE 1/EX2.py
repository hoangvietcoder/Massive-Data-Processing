x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
z = dict()

for key in x:
    if key in y and x[key] == y[key]:
        z[key] = x[key]

for myKey in list(z.keys()):
    print(myKey + ": " + str(z[myKey]), "is present in both x and y")
