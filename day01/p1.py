def p1():
    with open ("day1/input1") as f:
        list1 = []
        list2 = []
        for line in f:
            split = line.split('   ')
            list1.append(split[0])
            list2.append(split[1])
    list1.sort()
    list2.sort()
    distance = 0
    for i in range(len(list1)):
        distance += abs(int(list1[i]) - int(list2[i]))
    return distance