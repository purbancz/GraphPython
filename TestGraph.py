import unittest

from Graph import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_add_and_remove_node(self):
        self.graph.add_node('A')
        self.assertIn('A', self.graph.graph)
        self.graph.remove_node('A')
        self.assertNotIn('A', self.graph.graph)

    def test_add_and_remove_edge(self):
        self.graph.add_node('A')
        self.graph.add_node('B')
        self.graph.add_edge('A', 'B')
        self.assertIn('B', self.graph.graph['A'])
        self.assertIn('A', self.graph.graph['B'])
        self.graph.remove_edge('A', 'B')
        self.assertNotIn('B', self.graph.graph['A'])
        self.assertNotIn('A', self.graph.graph['B'])

    def test_get_neighbors(self):
        self.graph.add_node('A')
        self.graph.add_node('B')
        self.graph.add_edge('A', 'B')
        self.assertEqual(self.graph.get_neighbors('A'), ['B'])

    def test_bfs(self):
        self.graph.add_node('A')
        self.graph.add_node('B')
        self.graph.add_edge('A', 'B')
        bfs_iterator = self.graph.bfs('A')
        self.assertEqual(list(bfs_iterator), ['A', 'B'])

    def test_dfs(self):
        self.graph.add_node('A')
        self.graph.add_node('B')
        self.graph.add_edge('A', 'B')
        dfs_iterator = self.graph.dfs('A')
        self.assertEqual(list(dfs_iterator), ['A', 'B'])

if __name__ == '__main__':
    unittest.main()
