def strictIncr(li):
    for i in range(len(li)-1):
        if li[i] >= li[i+1]:
            return False
    return True

def strictDecr(li):
    for i in range(len(li)-1):
        if li[i] <= li[i+1]:
            return False
    return True

def maxDiff(li):
    for i in range(len(li)-1):
        diff = abs(li[i] - li[i+1])
        if diff < 1 or diff > 3:
            return False
    return True

def p1(reportsList):
    safeCount = 0  
    for line in reportsList:
        for el in range(len(line)):
            temp = [x for x in line]
            temp.pop(el)
            if (strictIncr(temp) or strictDecr(temp)) and maxDiff(temp):
                safeCount += 1
                break
    return safeCount


listInput = []
with open ("day02/input.txt") as f:
    for line in f:
        line = line.split()
        line = list(map(int, line))
        listInput.append(line)

print(p1(listInput))