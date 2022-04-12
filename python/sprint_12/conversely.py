# Comment it before submitting
# class DoubleConnectedNode:
#     def __init__(self, value, next=None, prev=None):
#         self.value = value
#         self.next = next
#         self.prev = prev


def solution(node):
    n = node.next # присвоили переменной n след.значение
    node.next = None # удалили инф. о след значении
    node.prev = n # следующее значение теперь стало предыдущим
    while n is not None: # пока у значения есть поле next
        n.prev = n.next # следующее значение теперь стало предыдущим
        n.next = node # ссылка на след.значение у след.значения == текущее значение
        node = n # теперь текущий node == следующему
        n = n.prev
    
    return node


def test():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    new_head = solution(node0)
    print(new_head.value)

#test()


    # result is new_head == node3
    # node3.next == node2
    # node2.next == node1 node2.prev == node3
    # node1.next == node0 node1.prev == node2
    # node0.prev == node1
