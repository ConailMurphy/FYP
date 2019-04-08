from SortingAlgorithms import swap
import string
from anytree import *


# tree node class for representing a node in a decision tree
class TreeNode:
    def __init__(self, parent, order, decision):
        self.parent = parent  # the parent node. None for the root node
        self.decision = decision  # a single comparison made by the algorithm eg. x > y
        self.order = order   # the order of the elements for the node eg. b c a
        self.left_child = None  # left children made a comparison such that x > y
        self.right_child = None  # right children made a comparison such that x < y
        self.data = []  # lists that belong in the current node

    # recursive function for adding nodes to a tree
    def add_node(self, parent_order, decisions, data):
        self.data.append(data)

        # used to determine if a node's order need to be changed
        order = list(parent_order)
        index_a = 0
        index_b = 0
        for i in range(len(parent_order)):
            if parent_order[i] == decisions[0][0]:
                index_a = i
            elif parent_order[i] == decisions[0][2]:
                index_b = i

        if decisions[0][1] == ">":
            if decisions[0][3] == "swap":
                # order should be changed to show that the algorithm swapped the elements that were compared
                swap(order, index_a, index_b)
            # if the node does not have a left child, create one
            if self.left_child is None:
                self.left_child = TreeNode(self, order, string.join(decisions[0]))

                # if there is more than one decision left in the list, call add_node on the newly created node
                if len(decisions) > 1:
                    decisions.pop(0)
                    self.left_child.add_node(order, decisions, data)
                else:
                    self.add_leaf_node_data(decisions, data)
            # if the node already has a left child, call add_node on it
            else:
                decisions.pop(0)
                self.left_child.add_node(order, decisions, data)
        else:
            if decisions[0][3] == "swap":
                # order should be changed to show that the algorithm swapped the elements that were compared
                swap(order, index_a, index_b)
            # if the node does not have a right child, create one
            if self.right_child is None:
                self.right_child = TreeNode(self, order, string.join(decisions[0]))
                # if there is more than one decision left in the list, call add_node on the newly created node
                if len(decisions) > 1:
                    decisions.pop(0)
                    self.right_child.add_node(order, decisions, data)
                # if only one decision is left, then the next node to be created is a leaf
                else:
                    self.add_leaf_node_data(decisions, data)
            # if the node already has a right child, call add_node on it
            else:
                decisions.pop(0)
                self.right_child.add_node(order, decisions, data)

    # adds a leaf node to a tree
    def add_leaf_node_data(self, decisions, data):

        if decisions[0][1] == ">":
            # update the order and create a left_child
            order = list(self.order)
            index_a = 0
            index_b = 0
            for i in range(len(self.order)):
                if self.order[i] == decisions[0][0]:
                    index_a = i
                elif self.order[i] == decisions[0][2]:
                    index_b = i
            swap(order, index_a, index_b)
            if not self.left_child:
                self.left_child = TreeNode(self, order, string.join(decisions[0]))
            self.left_child.data.append(data)
        else:
            # leave order unchanged and create a right_child
            if not self.right_child:
                self.right_child = TreeNode(self, self.order, string.join(decisions[0]))
            self.right_child.data.append(data)

    # prints the contents of a tree using the node that called the function as the root of the tree
    def print_tree(self):
        print(self.decision, self.order, self.data, )
        if self.left_child:
            self.left_child.print_tree()
        if self.right_child:
            self.right_child.print_tree()

    # recursive function for creating nodes in the graphic tree to be displayed
    def create_graphic_node(self, graphic_node):
        # fetches only the numeric component of each tuple stored in self.data
        data = []
        for i in self.data:
            temp_data = []
            for j in range(len(i)):
                temp_data.append(i[j][0])
            data.append(temp_data)

        # the root node of the will call create_graphic_node using
        # the length of the user input array a parameter
        if isinstance(graphic_node, int):
            # since a graphic nodes id is derived from it's parent.order
            # and the root node has no parent, it's id must be created from scratch
            order = ""
            for i in range(graphic_node):
                order = order + string.ascii_lowercase[i]
                if i < graphic_node - 1:
                    order = order + " "
            # anytree's RenderTree function prints the attributes names in alphabetical order
            # for this reason attribute names have a letter added to the start so tha they
            # are printed in the desired order
            new_graphic_node = AnyNode(parent=self.parent, a_decision=None, b_order=order, c_data=data)
        else:
            new_graphic_node = \
                AnyNode(parent=graphic_node, a_decision=self.decision, b_order=string.join(self.order), c_data=data)

        # recursively call create_graphic_node if the node has any child nodes
        if self.left_child:
            self.left_child.create_graphic_node(new_graphic_node)
        if self.right_child:
            self.right_child.create_graphic_node(new_graphic_node)
        return new_graphic_node
