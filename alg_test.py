import random


class Node:
    def __init__(self, num=0):
        if num == 0:
            self.value = random.randint(0, 20)
        else:
            self.value = num
        self.child_num = random.randint(0, 5)
        self.children = []

    def generate_children(self):
        for x in range(0, self.child_num):
            self.children.append(Node())

        return self.children

    @staticmethod
    def compare_node(node):
        return node.value


def alphabeta(node, depth, a, b, maximizing_player):
    if depth == 0 or node.child_num == 0:
        return node
    if maximizing_player:
        for child in node.generate_children():
            a = max(a, alphabeta(child, depth - 1, a, b, False), key=Node.compare_node)
            if b.value <= a.value:
                break
        return a
    else:
        for child in node.generate_children():
            b = min(b, alphabeta(child, depth - 1, a, b, True), key=Node.compare_node)
            if b.value <= a.value:
                break
        return b



print "\nAnswer: " + str(alphabeta(Node(), 4, Node(-99999999), Node(999999999), True).value)