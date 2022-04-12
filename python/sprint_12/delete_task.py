# Comment it before submitting
# class Node:
#     def __init__(self, value, next_item=None):
#         self.value = value
#         self.next_item = next_item


def get_node_by_idx(node, idx):
    while idx:
        node = node.next_item
        idx -= 1
    return node


def solution(node, idx):
    if idx == 0:
        following_node = get_node_by_idx(node, idx + 1)
        return following_node
    previous_node = get_node_by_idx(node, idx - 1)
    following_node = get_node_by_idx(node, idx + 1)
    previous_node.next_item = following_node
    return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 0)
    print(new_head.value)
    # result is node0 -> node2 -> node3


# test()
