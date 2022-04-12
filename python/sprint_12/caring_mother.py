# Comment it before submitting
# class Node:
#    def __init__(self, value, next_item=None):
#        self.value = value
#        self.next_item = next_item


def solution(node, elem):
    index = 0
    try:
        while node.value != elem:
            node = node.next_item
            index += 1
    except AttributeError:
        return "-1"
    return index


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node4")
    return idx

    # result is idx == 2


# print(test())
