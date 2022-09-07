def solution(l):
    intList = l
    luckyDoubles = [0] * len(intList)
    count = 0
    for i in range(0,len(intList)):
        j=0
        for j in range(0, i):
            if l[i] % l[j] == 0:
                luckyDoubles[i] = luckyDoubles[i] + 1
                count = count + luckyDoubles[j]
    return count

# print(solution([1, 8, 16, 32]))
print(solution([1,1,1]), 1)
                