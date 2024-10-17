from collections import Counter

def solution(boxes):
    item_count = dict()

    for box in boxes:
        item_count[box[0]] = item_count.get(box[0],0) + 1
        item_count[box[1]] = item_count.get(box[1],0) + 1


    odd_count = sum(1 for count in item_count.values() if count%2 != 0)
    print(item_count)
    return odd_count // 2

print(solution([[1,1],[2,3],[3,1]]))

