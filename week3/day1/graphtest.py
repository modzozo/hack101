from graph import DirectedGraph
import unittest


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.my_graph = DirectedGraph()

    def test_init(self):
        self.assertEqual(self.my_graph.nodes, {})

    def test_add_edge(self):
        self.my_graph.add_edge("modzozo", "RadoRado")
        self.assertEqual(self.my_graph.nodes, {"modzozo": ["RadoRado"], "RadoRado": []})

    def test_get_neighbours(self):
        self.my_graph.add_edge("modzozo", "RadoRado")
        self.my_graph.add_edge("modzozo", "mod")
        self.assertEqual(self.my_graph.get_neighbours_for("modzozo"), ["RadoRado", "mod"])

    def test_path_between_true(self):
        self.my_graph.add_edge("modzozo", "RadoRado")
        self.my_graph.add_edge("modzozo", "mod")
        self.my_graph.add_edge("RadoRado", "Rado")
        self.my_graph.add_edge("Rado", "zozo")
        self.assertTrue(self.my_graph.path_between("modzozo", "zozo"))

    def test_path_between_false(self):
        self.my_graph.add_edge("modzozo", "RadoRado")
        self.my_graph.add_edge("modzozo", "mod")
        self.my_graph.add_edge("RadoRado", "Rado")
        self.my_graph.add_edge("Rado", "zozo")
        self.assertFalse(self.my_graph.path_between("Rado", "modzozo"))

    def test_path_between_cycle(self):
        self.my_graph.add_edge("modzozo", "RadoRado")
        self.my_graph.add_edge("modzozo", "mod")
        self.my_graph.add_edge("RadoRado", "Rado")
        self.my_graph.add_edge("Rado", "zozo")
        self.my_graph.add_edge("zozo", "modzozo")
        self.assertTrue(self.my_graph.path_between("modzozo", "zozo"))

if __name__ == '__main__':
    unittest.main()
