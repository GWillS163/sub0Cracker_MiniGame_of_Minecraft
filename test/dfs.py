
graph = {
    "a": ["1", '2', '3'],
    "1": ["a", "b"],
    "2": ["a", "d"],
    "3": ["a", "c"],
    "b": ["1", "c"],
    "c": ["2", "b", "d"],
    # "d": ["3", "c"]
}


def dfs(map, start, end):
    stack = [start]
    visited = []
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.append(current)
        if current == end:
            return visited
        for node in map[current]:
            stack.append(node)
    return visited


print(list(dfs(graph, "a", "d")))

realData = {'3': ["4", [0, 5]],
 '2': ["3", [0, 5]],
 '[2, 1]': [[5, 1]],
 '[2, 5]': [[4, 5], [2, 0]],
 '4': ["5"],
 '5': [[2, 5], "6"],
 '7': [[2, 1], "8"],
 '6': ["7"],
 '[5, 0]': [[5, 2]],
 '8': [[5, 0], "9"],
 '9': [[0, 2], "10"],
 '1': ["2"]}


def dfs(map, start, end):
    stack = [start]
    visited = []
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.append(current)
        if current == end:
            return visited
        if str(current) not in map.keys():
            visited.remove(current)
            continue
        for node in map[current]:
            stack.append(str(node))
    return visited


print(list(dfs(realData,  '1', "10")))
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
            continue
        for node in map[str(current)]:
            stack.append(node)
    return visited

realData2 = {'[0, 0]': [[3, 0], [0, 5]],
 '[0, 4]': [[0, 0], [0, 5]],
 '[2, 1]': [[5, 1]],
 '[2, 5]': [[4, 5], [2, 0]],
 '[3, 0]': [[3, 5]],
 '[3, 5]': [[2, 5], [4, 5]],
 '[4, 1]': [[2, 1], [5, 1]],
 '[4, 5]': [[4, 1]],
 '[5, 0]': [[5, 2]],
 '[5, 1]': [[5, 0], [5, 2]],
 '[5, 2]': [[0, 2], [1, 2]],
 '[5, 4]': [[0, 4]]}

print(list(dfs(realData2,  [5, 4], [1, 2])))