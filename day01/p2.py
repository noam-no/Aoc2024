def p2():
    with open ("day1/input1") as f:
        list1 = []
        list2 = []
        for line in f:
            split = line.split('   ')
            list1.append(int(split[0]))
            list2.append(int(split[1]))
    similarity = 0
    for i in range(len(list1)):
        similarity += list1[i]*list2.count(list1[i])

    return similarity

print(p2())