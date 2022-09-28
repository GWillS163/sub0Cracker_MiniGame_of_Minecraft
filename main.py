

from pprint import pprint


def getNearestPosition(maps: list, current: list):
    """
    得到下一步节点

    :param maps:
    :param current:
    :return:
    """
    maxWidth = len(maps[0])
    maxHeight = len(maps)
    res = []
    withoutDuplicate = []
    # 1. get the nearest position
    # up
    for row in range(current[0], 0 - 1, -1):
        if maps[row][current[1]] == 1:
            res.append([row + 1, current[1]])
            break
        elif row == 0:
            res.append([row, current[1]])

    # down
    for row in range(current[0], maxHeight):
        if maps[row][current[1]] == 1:
            res.append([row - 1, current[1]])
            break
        elif maps[row][current[1]] == 0 and row == maxHeight - 1:
            res.append([row, current[1]])

    # left
    for col in range(current[1], 0 - 1, -1):
        if maps[current[0]][col] == 1:
            res.append([current[0], col + 1])
            break
        elif col == 0:
            res.append([current[0], col])

    # right
    for col in range(current[1], maxWidth):
        if maps[current[0]][col] == 1:
            res.append([current[0], col - 1])
            break
        elif maps[current[0]][col] == 0 and col == maxWidth - 1:
            res.append([current[0], col])

    # 去除重复的节点 - get rid of the duplicate node
    for nextHop in res:
        if nextHop in withoutDuplicate or nextHop == current:
            continue
        withoutDuplicate.append(nextHop)
    return withoutDuplicate


def dfs(map: dict, start: list, end: list) -> list:
    # TODO: 非最短路径
    stack = [start]
    visited = []
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.append(current)
        if str(current) == str(end):
            return visited
        if str(current) not in map.keys():
            visited.remove(current)
            continue
        for node in map[str(current)]:
            stack.append(node)
    return visited


def findOptimizePath(graph: dict, stt: list, end: list):
    path, cost = spf(graph, stt, end)
    return path


def spf(graph: dict, stt: list, end: list, sttCost=0):  # -> List[List[int]]:
    # get stt up
    if str(stt) == str(end):
        return [stt], sttCost + 1
    if str(stt) not in graph.keys():
        return [], sttCost + 1

    nextHops = graph[str(stt)]
    pathDict = {}
    for nextHop in nextHops:
        (path, cost) = spf(graph, nextHop, end, sttCost)
        if not path:
            continue
        # There cost maybe not correct
        pathDict.update({cost: [stt] + path})
    if not pathDict:
        return [], 99
    return pathDict[min(pathDict.keys())], min(pathDict.keys())


def getKey(graph: dict, currentNode: list):
    res = []
    for key, value in graph.items():
        if currentNode in value:
            res.append(eval(key))
    return res


def isPassEnd(current, nextHop, end):
    """
    判断是否途径终点, 如下例子通过current节点可能是 5,2  NextHop 是0,2 and 终点is 1,2
    Judge if it is pass the end point, maybe current is 0, 5, NextHop is 0,2 and end is 1,2
    :param nextHop:
    :param end:
    :return:
    """
    # 判断是否是同一行 - judge if it is in the same row
    if current[0] == nextHop[0] and current[0] == end[0]:
        # 向上走是否路过终点 - judge if it is pass the end point when it is going up
        if current[1] < end[1] <= nextHop[1]:
            return True
        # 向下走是否路过终点 - judge if it is pass the end point when it is going down
        elif current[1] > end[1] >= nextHop[1]:
            return True
    # 判断是否是同一列 - judge if it is in the same column
    elif current[1] == nextHop[1] and current[1] == end[1]:
        # 向上走是否路过 - judge if it is pass the end point when it is going up
        if current[0] < end[0] <= nextHop[0]:
            return True
        # 向下走是否路过终点 - judge if it is pass the end point when it is going down
        elif current[0] > end[0] >= nextHop[0]:
            return True
    return False


def findPathGraph(map2D: list, start: list, end: list):
    queue = []
    visited = []
    queue.append(start)
    graph = {}
    while queue:
        # 拿出之前的节点 - get the previous node
        currentNode = queue.pop(0)
        if currentNode in visited:
            continue
        visited.append(currentNode)
        # 添加相邻的节点 - add the nearest node (next Hop)
        nearestList = getNearestPosition(map2D, currentNode)
        for nextHop in nearestList:
            if not nextHop:
                continue
            if nextHop in visited:
                continue
            queue.append(nextHop)
            # 本次节点处理 - current node process
            if str(currentNode) not in graph.keys():
                graph.update({str(currentNode): []})
            graph[str(currentNode)].append(nextHop)
            # 判断是否到达终点 - judge if it is the end point
            if isPassEnd(currentNode, nextHop, end):
                if end not in graph[str(currentNode)]:
                    graph[str(currentNode)].append(end)
                break
    return graph


def mapAddArrow(map2D, stepList):
    last = stepList[0]
    for curr in stepList[1:]:
        # up
        if last[1] == curr[1] and last[0] > curr[0]:
            for row in range(curr[0], last[0]):
                map2D[row][last[1]] = "↑"
        # down
        elif last[1] == curr[1] and last[0] < curr[0]:
            for row in range(last[0], curr[0]):
                map2D[row][last[1]] = "↓"
        # left
        elif last[0] == curr[0] and last[1] > curr[1]:
            for col in range(curr[1], last[1]):
                map2D[last[0]][col] = "←"
        # right
        elif last[0] == curr[0] and last[1] < curr[1]:
            for col in range(last[1], curr[1]):
                map2D[last[0]][col] = "→"
        else:
            raise Exception(f"error: {last} -> {curr}")
        last = curr
    return map2D


def printAnsInMap(map2D, answerList, stt, end):
    map2D[stt[0]][stt[1]] = "S"
    map2D[end[0]][end[1]] = "E"
    if not answerList:
        printMap(map2D)
        print(f"\033[1;31;40m{stt} -> {end} is not reachable\033[0m")
        return
    map2D = mapAddArrow(map2D, answerList)
    step = ["①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨", "⑩", "⑪", "⑫", "⑬", "⑭", "⑮", "⑯", "⑰", "⑱", "⑲", "⑳"]
    n = 0
    for ans in answerList[1:]:
        map2D[ans[0]][ans[1]] = step[n]
        n += 1
    print("that is also as following graph shown:\n")
    # print(f"　", end="")
    printMap(map2D)
    print("")
    print("_" * 40 )

    # pprint(map2D)

def printMap(map2D):
    for colN in range(len(map2D[0])):
        print(f"\t{colN}", end="")
    print("")
    rowN = 0
    for row in map2D:
        print(rowN, "\t", end="")
        rowN += 1
        for cell in row:
            if cell == 1:
                print("■", end="\t")
            elif cell == 0:
                print("　", end="\t")
            else:
                print(cell, end="\t")
        print("")


def getSttAndEnd(map_lv):
    """
    自动识别6为起点，9为终点
    auto recognize 6 as start point and 9 as end point
    :param map_lv:
    :return:
    """
    stt, end = [], []
    for row in range(len(map_lv)):
        for col in range(len(map_lv[row])):
            if map_lv[row][col] == 6:
                stt = [row, col]
            elif map_lv[row][col] == 9:
                end = [row, col]
    return stt, end


def main(map_lv, mapName=""):
    print("MAP: ", mapName)
    stt, end = getSttAndEnd(map_lv)
    print("Stt: ", stt,
          "\nEnd: ", end)
    nodeGraph = findPathGraph(map_lv, stt, end)
    if nodeGraph is None:
        print("No path")
        exit(0)
    # pprint(nodeGraph)
    optimizePath = findOptimizePath(nodeGraph, stt, end)
    # optimizePath = dfs(nodeGraph, stt, end)
    print("path: ", optimizePath)
    print("step: ", len(optimizePath))
    printAnsInMap(map_lv, optimizePath, stt, end)

