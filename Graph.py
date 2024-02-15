from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    # def remove_node(self, node):
    #     if node in self.graph:
    #         del self.graph[node]
    #         for nodes in self.graph.values():
    #             if node in nodes:
    #                 nodes.remove(node)
    #     else:
    #         raise ValueError(f"Node {node} does not exist.")
    
    def remove_node(self, node):
        if node in self.graph:
            neighbors = self.graph[node]
            del self.graph[node]
            for neighbor in neighbors:
                self.graph[neighbor].remove(node)
        else:
            raise ValueError(f"Node {node} does not exist.")


    def add_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            if node2 not in self.graph[node1]:
                self.graph[node1].append(node2)
                self.graph[node2].append(node1)
            else:
                raise ValueError(f"Edge between {node1} and {node2} already exists.")
        else:
            raise ValueError(f"One or both nodes do not exist.")

    def remove_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            if node2 in self.graph[node1]:
                self.graph[node1].remove(node2)
                self.graph[node2].remove(node1)
            else:
                raise ValueError(f"Edge between {node1} and {node2} does not exist.")
        else:
            raise ValueError(f"One or both nodes do not exist.")

    def get_neighbors(self, node):
        if node in self.graph:
            return self.graph.get(node, [])
        else:
            raise ValueError(f"Node {node} does not exist.")

    def bfs(self, start_node):
        return BfsIterator(self.graph, start_node)

    def dfs(self, start_node):
        return DfsIterator(self.graph, start_node)


class BfsIterator:
    def __init__(self, graph, start_node):
        self.visited = []
        self.queue = deque([start_node])
        self.graph = graph

    def __iter__(self):
        return self

    def __next__(self):
        while self.queue:
            node = self.queue.popleft()
            if node not in self.visited:
                self.visited.append(node)
                neighbors = self.graph[node]
                for neighbor in neighbors:
                    self.queue.append(neighbor)
                return node
        raise StopIteration


class DfsIterator:
    def __init__(self, graph, start_node):
        self.visited = []
        self.stack = [start_node]
        self.graph = graph

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            node = self.stack.pop()
            if node not in self.visited:
                self.visited.append(node)
                neighbors = self.graph[node]
                for neighbor in neighbors:
                    self.stack.append(neighbor)
                return node
        raise StopIteration


if __name__ == "__main__":
    graph = Graph()

    graph.add_node('root')
    graph.add_node('left')
    graph.add_node('right')
    graph.add_node('leftleft')
    graph.add_node('leftright')
    graph.add_node('rightleft')
    graph.add_node('rightright')
    graph.add_node('3rdright')

    graph.add_edge('root', 'left')
    graph.add_edge('root', 'right')
    graph.add_edge('left', 'leftleft')
    graph.add_edge('left', 'leftright')
    graph.add_edge('right', 'rightleft')
    graph.add_edge('right', 'rightright')
    graph.add_edge('right', '3rdright')

    for node in graph.graph.items():
        print(node)

    print('-------------')

    print(graph.get_neighbors('left'))

    print('-------------')

    for vertex in graph.dfs('rightright'):
        print(vertex)

    print('-------------')

    for vertex in graph.bfs('rightright'):
        print(vertex)

    print('-------------')

    graph.remove_node('right')
    print('Node "right" removed')

    print('-------------')

    for vertex in graph.dfs('rightright'):
        print(vertex)

    print('-------------')

    for vertex in graph.bfs('rightright'):
        print(vertex)
