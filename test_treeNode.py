from unittest import TestCase, main
import DecisionTree as dT
import string


class TestTreeNode(TestCase):

    def setUp(self):
        print "Set up"
        self.root = dT.TreeNode(None, ("a", "b", "c"), [("a", ">", "b")])

    def tearDown(self):
        print "Tear down", "\n"

    def test_add_node(self):
        print "testing add_node"
        root = self.root
        root.add_node(root.order, root.decision, [2, 1, 3])
        self.assertEqual(root.left_child.parent, root)
        self.assertEqual(root.left_child.decision, string.join(root.decision[0]))
        self.assertEqual(root.left_child.order, ["b", "a", "c"])
        self.assertEqual(root.left_child.left_child, None)
        self.assertEqual(root.left_child.right_child, None)
        self.assertEqual(root.left_child.data, root.data)

    def test_create_graphic_node(self):
        print "testing create_graphic_node"
        root = self.root
        root.add_node(root.order, root.decision, [(2, "a"), (1, "b"), (3, "c")])

        graphic_node = root.create_graphic_node(3)

        self.assertEqual(graphic_node.parent, None)
        self.assertFalse(not graphic_node.children)
        self.assertEqual(graphic_node.children[0].parent, graphic_node)
        self.assertEqual(graphic_node.id, "a b c")
        self.assertEqual(graphic_node.j_data[0], [2, 1, 3])
        self.assertEqual(graphic_node.children[0].id, "b a c")
        self.assertEqual(graphic_node.children[0].j_data[0], [2, 1, 3])


if __name__ == '__main__':
    main()
