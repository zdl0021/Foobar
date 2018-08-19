#def answer(entrances, exits, path):
#    totalBunnies = 0
#    visited = []
#    capacities = []
#    for i in range(len(path)):
#        capacities.append(0)
#    for ent in entrances[:]:
#        for i in range(len(path[ent])):
#            if path[ent][i] > 0:
#                capacities[i] += path[ent][i]
#                path[ent][i] = 0
#        visited.append(ent)
#    while True:
#        pos = 0
#        while pos < len(path):
#            if visited.count(pos) == 0:
#                inflow = False
#                for i in range(len(path)):
#                    if path[i][pos] > 0:
#                        inflow = True
#                        break
#                if inflow == False:
#                    break
#            pos += 1
#        if pos == len(path):
#            break
#        while visited.count(pos) == 0:
#            maxFlow = max(path[pos])
#            if maxFlow == 0:
#                visited.append(pos)
#                break
#            pos2 = path[pos].index(maxFlow)
#            if visited.count(pos2) == 0:
#                if maxFlow > capacities[pos]:
#                    capacities[pos2] += capacities[pos]
#                    capacities[pos] = 0
#                else:
#                    capacities[pos] -= maxFlow
#                    capacities[pos2] += maxFlow
#                path[pos][pos2] = 0
#                if path[pos].count(0) == len(path[pos]) or capacities[pos] == 0:
#                    visited.append(pos)
#            else:
#                path[pos][pos2] = 0
#    for ex in exits[:]:
#        totalBunnies += capacities[ex]
#    return totalBunnies

#def answerAugm(entrances, exits, path):
#    augmentPath = []
#    totalBunnies = 0
#    zeroOut = []
#    while True:
#        minFlow = 0
#        for ent in entrances[:]:
#            if zeroOut.count(ent) == 0:
#                flowPath = [ent]
#                pos = 0
#            while len(flowPath) > 0:
#                i = pos
#                while i < len(path[flowPath[-1]]):
#                    if path[flowPath[-1]][i] > 0 and flowPath.count(i) == 0 and path[flowPath[-1]][i] > minFlow and zeroOut.count(i) == 0:
#                        flowPath.append(i)
#                        break
#                    i += 1
#                if exits.count(flowPath[-1]):
#                    current = []
#                    for j in range(len(flowPath) - 1):
#                        current.append(path[flowPath[j]][flowPath[j + 1]])
#                    tempMinFlow = min(current)
#                    if tempMinFlow > minFlow:
#                        minFlow = tempMinFlow
#                        augmentPath = []
#                        for elem in flowPath[:]:
#                            augmentPath.append(elem)
#                    pos = flowPath[-1] + 1
#                    flowPath.pop()
#                elif i == len(path[flowPath[-1]]):
#                    pos = flowPath[-1] + 1
#                    flowPath.pop()
#                else:
#                    pos = 0
#        for i in range(len(augmentPath) - 1):
#            path[augmentPath[i]][augmentPath[i + 1]] -= minFlow
#            if path[augmentPath[i]].count(0) == len(path[augmentPath[i]]):
#                zeroOut.append(augmentPath[i])
#            path[augmentPath[i + 1]][augmentPath[i]] += minFlow
#        if minFlow == 0:
#            break
#        totalBunnies += minFlow
#    return totalBunnies

def BFS(entrances, exits, path, augmentPath):
    traversed = [False] * len(path)
    queue = []
    qPos = 0
    result = [-1, -1]
    for ent in entrances[:]:
        queue.append(ent)
        traversed[ent] = True
    while qPos != len(queue):
        for i in range(len(path[queue[qPos]])):
            if traversed[i] == False and path[queue[qPos]][i] > 0:
                queue.append(i)
                traversed[i] = True
                augmentPath[i] = queue[qPos]
        qPos += 1

    for ex in exits[:]:
        if traversed[ex]:
            ent = augmentPath[ex]
            while augmentPath[ent] != -1:
                ent = augmentPath[ent]
            result[0] = ent
            result[1] = ex
    return result

def answer(entrances, exits, path):
    augmentPath = [-1] * len(path)
    totalBunnies = 0
    while True:
        st = BFS(entrances, exits, path, augmentPath)
        if st == [-1, -1]:
            break
        minFlow = float('Inf')
        s = st[0]
        t = st[1]
        while t != s:
            minFlow = min(minFlow, path[augmentPath[t]][t])
            t = augmentPath[t]
        totalBunnies += minFlow
        t = st[1]
        while t != s:
            path[augmentPath[t]][t] -= minFlow
            path[t][augmentPath[t]] += minFlow
            t = augmentPath[t]
    return totalBunnies



l = input().split()
entrances = []
for x in l[:]:
    entrances.append(int(x))
l = input().split()
exits = []
for x in l[:]:
    exits.append(int(x))
size = int(input())
path = []
for i in range(size):
    tempList = []
    l = input().split()
    for y in l[:]:
        tempList.append(int(y))
    path.append(tempList)
#print(answerAugm(entrances, exits, path))
print(answer(entrances, exits, path))

