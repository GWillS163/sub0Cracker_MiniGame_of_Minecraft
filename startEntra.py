#  Author : Github: @GWillS163
#  Time: $(Date)
from main import *

if __name__ == '__main__':
    maps_lv9 = [[0, 1, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0]]
    map_lv10 = [  # turn it to digital map with a list
        [0, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 1],
        [0, 9, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1]
    ]
    map_lv11 = [
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0],
        [1, 9, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 6, 0, 0]]
    map_lv12 = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1],
        [1, 0, 0, 9, 0, 1],
        [0, 0, 1, 0, 0, 0],
        [6, 1, 0, 1, 0, 0]]

    map_lv13 = [
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0],
        [9, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [6, 1, 0, 0, 0, 0],
    ]
    map_lv14 = [
        [9, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [6, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    # main(maps_lv10, [5, 4], [1, 2])
    # main(map_lv11, [3, 0], [1, 2])
    map_lv15 = [
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
    ]
    map_lv16 = [  # TODO: 第二步是冗余的
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    map_lv17 = [
        [0, 0, 0, 1, 0, 0, 1, 9],
        [0, 0, 6, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0]
    ]
    map_lv18 = [
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 9, 1],
        [6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]

    # main(map_lv10, "10")
    # main(map_lv11, "11")
    # main(map_lv12, "12")
    # main(map_lv13, "13")
    # main(map_lv14, "14")
    # main(map_lv15, "15")
    # main(map_lv16, "16")
    main(map_lv17, "17")
    printMap(map_lv17)
    # main(map_lv18, "18")
