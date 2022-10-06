#  Author : Github: @GWillS163
#  Time: $(Date)

#  Author : Github: @GWillS163
#  Time: $(Date)

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
    res = [[], [], [], []]
    withoutDuplicate = []
    # 1. get the nearest position
    # up
    for row in range(current[0], 0 - 1, -1):
        if maps[row][current[1]] == 1:
            res[0] = [row + 1, current[1]]
            break
        elif row == 0:
            res[0] = [row, current[1]]

    # down
    for row in range(current[0], maxHeight):
        if maps[row][current[1]] == 1:
            res[1] = [row - 1, current[1]]
            break
        elif maps[row][current[1]] == 0 and row == maxHeight - 1:
            res[1] = [row, current[1]]

    # left
    for col in range(current[1], 0 - 1, -1):
        if maps[current[0]][col] == 1:
            res[2] = [current[0], col + 1]
            break
        elif col == 0:
            res[2] = [current[0], col]

    # right
    for col in range(current[1], maxWidth):
        if maps[current[0]][col] == 1:
            res[3] = [current[0], col - 1]
            break
        elif maps[current[0]][col] == 0 and col == maxWidth - 1:
            res[3] = [current[0], col]

    # 去除重复的节点 - get rid of the duplicate node
    for nextHop in res:
        if nextHop in withoutDuplicate or nextHop == current:
            continue
        withoutDuplicate.append(nextHop)
    return withoutDuplicate


def getShortestPath(graphs: dict, stt: list, end: list):
    """
    Input start Node , end Node
    :param graphs:
    :param stt:
    :param end:
    :return:
    """
    queue = [stt]
    visited = []
    res = [stt]
    costList = {str(stt): [0, stt]}
    while queue:
        currentNode = list(queue.pop())
        if currentNode in visited:
            continue
        visited.append(currentNode)

        # 添加相邻的节点 - add the adjacent node
        if not str(currentNode) in graphs.keys():
            continue
        for node in graphs[str(currentNode)]:
            queue.append(node)
            if node in visited:
                continue
            lastCost = costList[str(currentNode)][0]
            costList.update({str(node): []})
            costList[str(node)] = [lastCost + 1, currentNode]

    return costList

def dfs(map: dict, start: list, end: list) -> list:
    stack = [start]
    visited = []
    optimizePath = []
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


def findOptimizationPath(map2D: list, start: list, end: list):
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
            if nextHop in visited:
                continue
            queue.append(nextHop)
            # 本次节点处理 - current node process
            if str(currentNode) not in graph.keys():
                graph.update({str(currentNode): []})
            graph[str(currentNode)].append(nextHop)
            # 判断是否到达终点 - judge if it is the end point
            if isPassEnd(currentNode, nextHop, end):
                graph[str(currentNode)].append(end)
                break
    return graph


def printAnsInMap(map2D, answerList):
    print(answerList)
    for ans in answerList:
        map2D[ans[0]][ans[1]] = "▣"

    for row in map2D:
        for cell in row:
            print(cell, "\t", end="")
        print("")
    # pprint(map2D)


def main(map_lv, start: list, end: list):
    nodeGraph = findOptimizationPath(map_lv, start, end)
    if nodeGraph is None:
        print("No path")
        exit(0)
    optimizePath = dfs(nodeGraph, start, end)
    printAnsInMap(map_lv, optimizePath)


if __name__ == '__main__':
    graph = {'[0, 0]': [[3, 0]],
             '[0, 4]': [[4, 4]],
             '[0, 5]': [[5, 5], [0, 4]],
             '[1, 0]': [[1, 2]],
             '[1, 1]': [[5, 1], [1, 0], [1, 2]],
             '[1, 2]': [[0, 2]],
             '[2, 0]': [[0, 0], [3, 0], [2, 5]],
             '[2, 3]': [[2, 0], [2, 5]],
             '[2, 5]': [[0, 5], [5, 5]],
             '[3, 0]': [[3, 5]],
             '[3, 5]': [],
             '[4, 1]': [[1, 1], [5, 1], [4, 5]],
             '[4, 4]': [[4, 1], [4, 5]],
             '[4, 5]': [],
             '[5, 0]': [[5, 3]],
             '[5, 1]': [],
             '[5, 3]': [[2, 3]],
             '[5, 5]': []}
    maps_lv10 = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1]]

    main(maps_lv10, [5, 4], [1, 2])

