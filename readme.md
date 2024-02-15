# Graph Implementation in Python

[![github](https://img.shields.io/badge/GitHub-purbancz-181717.svg?style=flat&logo=github)](https://github.com/purbancz)
[![x](https://img.shields.io/badge/Twitter-@purbancz-00aced.svg?style=flat&logo=x)](https://twitter.com/purbancz)
[![linkedin](https://img.shields.io/badge/LinkedIn-Piotr_Urbańczyk-00aced.svg?style=flat&logo=linkedin)](https://www.linkedin.com/in/piotr-urba%C5%84czyk-9943ab17a/)
[![website](https://img.shields.io/badge/Website-Piotr_Urbańczyk-5087B2.svg?style=flat&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHg9IjBweCIgeT0iMHB4IiB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGQ9Ik0gMTIgMi4wOTk2MDk0IEwgMSAxMiBMIDQgMTIgTCA0IDIxIEwgMTAgMjEgTCAxMCAxNCBMIDE0IDE0IEwgMTQgMjEgTCAyMCAyMSBMIDIwIDEyIEwgMjMgMTIgTCAxMiAyLjA5OTYwOTQgeiIgZmlsbD0iI2ZmZiI+PC9wYXRoPgo8L3N2Zz4=)](https://www.copernicuscenter.edu.pl/en/person/urbanczyk-piotr-2/)

This code implements a simple unweighted, undirected graph data structure in Python. It also includes iterators for breadth-first search (BFS) and depth-first search (DFS) traversals.

## Overview
The project consists of three main components:
-  `Graph`: A class that represents a graph. The graph is stored as an adjacency list, where each node maps to a list of its neighbors.
-  `BfsIterator` and `DfsIterator` classes that allow for iterating over the graph in a Breadth-First Search (BFS) and Depth-First Search (DFS) manner respectively.

## Features
- Add and remove nodes from the graph.
- Add and remove edges between nodes in the graph.
- Get the neighbors of a given node.
- Perform a breadth-first search (BFS) or depth-first search (DFS) on the graph.

## Usage  
```python
g = Graph()

g.add_node('A')
g.add_node('B')

bfs_iterator = g.bfs('A')
for node in bfs_iterator:
	print(node)

dfs_iterator = g.dfs('A')
for node in dfs_iterator:
	print(node)
```