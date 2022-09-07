def solution(pellets):
    pellets = int(pellets)
    gen = 0
    while True:
        if pellets == 1:
            return gen
        if pellets % 2 == 0:
            pellets /= 2
            gen += 1
        else:
            add = pellets+1
            remove = pellets-1
            counterAdd = 0
            counterRemove = 0
            while True:
                if add % 2 == 0:
                    add /= 2
                    counterAdd+=1
                if remove % 2 == 0:
                    remove /= 2
                    counterRemove += 1
                if add % 2 == 1 and remove % 2 == 1 or (add == 1 or remove == 1):
                    break
            if counterAdd > counterRemove:
                pellets +=1
                gen += 1
                for x in range(counterAdd):
                    pellets /= 2
                    gen +=1
            else:
                pellets -= 1
                gen += 1
                for x in range(counterRemove):
                    pellets /= 2
                    gen +=1
        if pellets == 1:
            return gen
                


print(solution(3), 2)
#print(solution(), 5)