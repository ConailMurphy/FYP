from anytree import AnyNode, RenderTree


class DecisionTree:
    def __init__(self):
        # When rendering a tree, anytree prints the attributes of a node in alphabetical order
        # for this reason, order and data became j_order and k_data respectively
        # so they would be printed in the desired order

        # d refers to the depth of a node
        # eg. d3_llr is at depth 3

        # l and r refer to the edges to be followed from the root to reach a node
        # eg. d3_llr is reached by following left at depth 0, left at depth 1 and right at depth 2

        # the id attribute represents the result of the comparison made at the parent node (excluding the root node)

        # depth 0 node
        self.root =  AnyNode(id="root", j_order="abc", k_data=[])

        # depth 1 nodes
        self.d1_l = AnyNode(id="a<b", parent=self.root, j_order="abc", k_data=[])
        self.d1_r = AnyNode(id="a>b", parent=self.root, j_order="bac", k_data=[])

        # depth 2 nodes
        self.d2_ll = AnyNode(id="b<c;", parent=self.d1_l, j_order="abc", k_data=[])
        self.d2_lr = AnyNode(id="b>c", parent=self.d1_l, j_order="acb", k_data=[])
        self.d2_rl = AnyNode(id="a<c", parent=self.d1_r, j_order="bac", k_data=[])
        self.d2_rr = AnyNode(id="a>c", parent=self.d1_r, j_order="bca", k_data=[])

        # depth 3 nodes
        self.d3_lll = AnyNode(id="a<b", parent=self.d2_ll, j_order="abc", k_data=[])
        # impossible for both a<b and a>b to be true so k_data will be None
        self.d3_llr = AnyNode(id="a>b", parent=self.d2_ll, j_order=None, k_data=None)
        self.d3_lrl = AnyNode(id="a<c", parent=self.d2_lr, j_order="acb", k_data=[])
        self.d3_lrr = AnyNode(id="a>c", parent=self.d2_lr, j_order="cab", k_data=[])
        self.d3_rll = AnyNode(id="b<a", parent=self.d2_rl, j_order="bac", k_data=[])
        # impossible for both a<b and a>b to be true so k_data will be None
        self.d3_rlr = AnyNode(id="b>a", parent=self.d2_rl, j_order=None, k_data=None)
        self.d3_rrl = AnyNode(id="b<c", parent=self.d2_rr, j_order="bca", k_data=[])
        self.d3_rrr = AnyNode(id="b>c", parent=self.d2_rr, j_order="cba", k_data=[])

        self.leaves = [self.d3_lll, self.d3_llr, self.d3_lrl,self.d3_lrr
                , self.d3_rll, self.d3_rlr, self.d3_rrl, self.d3_rrr]


# appends to the k_data attribute of the specified node
# if the node has a parent, the function is recursively called using the parent node
def append_data(node, data):
    node.k_data.append(data)
    if node.parent is not None:
        append_data(node.parent, data)