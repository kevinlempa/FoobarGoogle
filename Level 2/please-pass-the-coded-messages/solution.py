def solution(l):
    l.sort(reverse = True)
    nString = ""
    for i in l:
        nString += str(i)
    lenght = len(l)
    s = sum(l)
    
    if s % 3 == 0:
        return int(nString)
   
    elif s % 3 == 1:
        
        i = lenght - 1
        while i >= 0:
            if l[i] % 3 == 1:
                return int(nString[:i] + nString[i+1:])
            i -= 1
       
        i = lenght - 1
        while i >= 0:
            if l[i] % 3 == 2:
                break
            i -= 1
        j = i - 1
        while j >= 0:
            if l[j] % 3 == 2:
                break
            j -= 1
        if j == 0 and i == 1:
            return 0
        return int(nString[:j] + nString[j+1:i] + nString[i+1:])
    else:
        
        i = lenght - 1
        while i >= 0:
            if l[i] % 3 == 2:
                return int(nString[:i] + nString[i+1:])
            i -= 1
       
        i = lenght - 1
        while i >= 0:
            if l[i] % 3 == 1:
                break
            i -= 1
        j = i - 1
        while j >= 0:
            if l[j] % 3 == 1:
                break
            j -= 1
        if j == 0 and i == 1:
            return 0
        return int(nString[:j] + nString[j+1:i] + nString[i+1:])
print(solution([4,4])) 