# class Node:
#    def __init__(self, value, next_item=None):
#        self.value = value
#        self.next_item = next_item
#
#
# def define_my_define(node):
#    while node:
#        print(node.value)
#        node = node.next_item


def get_node_by_index(node, index):
    while index:
        node = node.next_item
        index -= 1
    return node


def solution(head, index):
    if index == 0:
        following_node = get_node_by_index(head, index + 1)
        return following_node
    previous_node = get_node_by_index(head, index - 1)
    following_node = get_node_by_index(head, index + 1)
    previous_node.next_item = following_node
    return head


def test():
    node4 = Node("node4!", None)
    node3 = Node("node3", node4)
    node2 = Node("node2", node3)
    new_node = Node("new node MF!!!", node2)
    node1 = Node("node1", new_node)
    node0 = Node("node0", node1)
    node00 = Node("node00", node0)

    index = 3
    value = "NEWWEST NODE!!!!"
    a = solution(node00, index)
    res = define_my_define(a)
    return res


print(test())
