def Add(bigIntA, bigIntB):

    if len(bigIntA) < len(bigIntB):
        temp = bigIntA
        bigIntA = bigIntB
        bigIntB = temp

    bigIntA_reverse = bigIntA[::-1]
    bigIntB_reverse = bigIntB[::-1]

    if len(bigIntA_reverse) > len(bigIntB_reverse):
        for i in range(len(bigIntA_reverse) - len(bigIntB_reverse)):
            bigIntB_reverse += "0"

    result = ""
    r = 0

    for i in range(len(bigIntA_reverse)):
        Sum = int(bigIntA_reverse[i]) + int(bigIntB_reverse[i]) + r
        r = 0
        if int(Sum) >= 10:
            r = Sum // 10
        result += str(Sum % 10)

    if r > 0:
        result += str(r)

    return result[::-1]


print(Add("246813579135792468123456789", "123456789135792468246813579"))


def Sub(bigIntA, bigIntB):

    bigIntA_reverse = bigIntA[::-1]
    bigIntB_reverse = bigIntB[::-1]

    if len(bigIntA_reverse) > len(bigIntB_reverse):
        for i in range(len(bigIntA_reverse) - len(bigIntB_reverse)):
            bigIntB_reverse += "0"

    if len(bigIntA_reverse) < len(bigIntB_reverse):
        for i in range(len(bigIntB_reverse) - len(bigIntA_reverse)):
            bigIntA_reverse += "0"

    result = ""
    r = 0

    for i in range(len(bigIntA_reverse)):
        temp_bigIntA = int(bigIntA_reverse[i])
        temp_bigIntB = int(bigIntB_reverse[i])
        if r > 0:
            temp_bigIntB += r
            r = 0
        if temp_bigIntA < temp_bigIntB:
            temp_bigIntA += 10
            r += 1
        result += str(temp_bigIntA - temp_bigIntB)

    for i in range(len(result) - 1, -1, -1):
        if result[i] == "0":
            result = result[:-1:]
        else:
            return result[::-1]


bigIntA = "246813579135792468123456789"
bigIntB = "123456789135792468246813579123456789"

if len(bigIntA) < len(bigIntB):
    print("-" + Sub(bigIntB, bigIntA))
else:
    print(Sub(bigIntA, bigIntB))
