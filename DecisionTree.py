from SortingAlgorithms import swap
import string
from anytree import *


class TreeNode:
    def __init__(self, parent, order, decision):
        self.parent = parent
        self.decision = decision
        self.order = order
        self.left_child = None
        self.right_child = None
        self.data = []

    def add_node(self, parent_order, decisions, data):
        self.data.append(data)
        order = parent_order
        index_a = 0
        index_b = 0
        for i in range(len(parent_order)):
            if parent_order[i] == decisions[0][0]:
                index_a = i
            elif parent_order[i] == decisions[0][2]:
                index_b = i

        if decisions[0][1] == ">":
            swap(order, index_a, index_b)
            # if the node does not have a left child, create one
            if self.left_child is None:
                self.left_child = TreeNode(self, order, string.join(decisions[0]))
                # if there are still decisions in the list, call add_node on the newly created node
                if len(decisions) > 1:
                    decisions.pop(0)
                    self.left_child.add_node(order, decisions, data)
                else:
                    self.left_child.add_leaf_node_data(decisions, data)
            # if the node already has a left child, call add_node on it
            else:
                decisions.pop(0)
                self.left_child.add_node(order, decisions, data)
        else:
            # if the node does not have a right child, create one
            if self.right_child is None:
                self.right_child = TreeNode(self, order, string.join(decisions[0]))
                # if there are still decisions in the list, call add_node on the newly created node
                if len(decisions) > 1:
                    decisions.pop(0)
                    self.right_child.add_node(order, decisions, data)
                else:
                    self.right_child.add_leaf_node_data(decisions, data)
            # if the node already has a right child, call add_node on it
            else:
                decisions.pop(0)
                self.right_child.add_node(order, decisions, data)

    def add_leaf_node_data(self, decisions, data):
        a = (data[0], "a")
        b = (data[1], "b")
        c = (data[2], "c")

        operand_1 = None
        operand_2 = None

        if decisions[0][0] == a[1]:
            operand_1 = a[0]
        elif decisions[0][0] == b[1]:
            operand_1 = b[0]
        elif decisions[0][0] == c[1]:
            operand_1 = c[0]

        if decisions[0][2] == a[1]:
            operand_2 = a[0]
        elif decisions[0][2] == b[1]:
            operand_2 = b[0]
        elif decisions[0][2] == c[1]:
            operand_2 = c[0]

        if operand_1 > operand_2:
            self.data.append(data)
        else:
            self.data.append(data)

    def print_tree(self):
        print(self.decision, self.data)
        if self.left_child:
            self.left_child.print_tree()
        if self.right_child:
            self.right_child.print_tree()

    def create_graphic_node(self, graphic_node):
        data = []
        for i in self.data:
            temp_data = []
            for j in range(len(i)):
                temp_data.append(i[j][0])
            data.append(temp_data)
        if isinstance(graphic_node, int):
            id = ""
            for i in range(graphic_node):
                id = id + string.ascii_lowercase[i]
                if i < graphic_node -1:
                    id = id + " "
            node = AnyNode(id=id, parent=self.parent, j_data=data)
        else:
            node = AnyNode(id=string.join(self.order), parent=graphic_node, j_data=data)
        if self.left_child:
            self.left_child.create_graphic_node(node)
        if self.right_child:
            self.right_child.create_graphic_node(node)
        return node