def solution(h, q):
    i = 0
    result = []
    for converter in q:
        i +=1
        maxId = 2**h-1
        prevNode = -1
        currentNode = maxId
        subtree = maxId
        
        if currentNode == converter:
            result.append(prevNode)
            

        prevNode = currentNode

        while subtree > 1:
            subtree = subtree >> 1

            left = currentNode - subtree - 1
            right = currentNode - 1

            if converter == left or converter == right:
                result.append(prevNode)
                break

            if converter < left:
                currentNode = left
            elif converter > left:
                currentNode = right

            prevNode = currentNode
        if i != len(result):
            result.append(-1)   
    return result

