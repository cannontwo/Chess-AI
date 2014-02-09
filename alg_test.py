import random


class Node:
    def __init__(self):
        self.value = random.randint(0, 20)
        self.child_num = random.randint(0, 5)
        self.children = []

    def generate_children(self):
        for x in range(0, self.child_num):
            self.children.append(Node())


def alphabeta(node, depth, a, b, maximizing_player):
    if depth == 0 or len(node.children) == 0:
        return node.value
    if maximizing_player:
        for child in node.generate_children():
            a = max(a, alphabeta(child, depth - 1, a, b, False))
            if b <= a:
                break
        return a
    else:
        for child in node.children:
            b = min(b, alphabeta(child, depth - 1, a, b, True))
            if b <= a:
                break
        return b

print alphabeta(Node(), 4, -99999999, 999999999, True)