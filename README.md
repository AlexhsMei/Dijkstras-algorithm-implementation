# Dijkstra's Algorithm — Python Project

**Authors:** 
* [Αλέξης Μειντάνης](https://github.com/AlexhsMei)
* [Γιώργος Ιωακείμαρος](https://github.com/ioakeimarosgiorgos)
  
## Overview

This first year Electrical Engineering university project is a simple implementation of **Dijkstra's shortest-path algorithm** in Python.

The program also includes a graph visualization, making it possible to see the generated graph, its edge weights, and the shortest path found by the algorithm.

## How It Works

The program:

1. Generates a weighted, undirected graph.
2. Assigns random weights to the edges.
3. Displays the graph and its edge weights.
4. Asks the user to enter a starting node and an ending node.
5. Runs Dijkstra's algorithm from the selected starting node.
6. Prints the shortest path to the selected ending node.
7. Displays the graph again with the shortest path highlighted in red.

The graph is generated randomly each time the program runs. This was added as an extra feature to demonstrate that the implementation is not dependent on one specific graph.

## Example of program results
<img width="700" alt="graph1" src="https://github.com/user-attachments/assets/d50658ca-e29f-4ce4-810f-7e59366bf3dc" />

> The randomized graph before applying the Dijkstra algorithm.
<br>
<br>
<img width="700" alt="graph2" src="https://github.com/user-attachments/assets/2ce3f4b9-f0ac-4a3d-8ff1-da6881602626" />

> The solved graph after choosing start & end for the algorithm

## Requirements

- Python 3
- `networkx`
- `matplotlib`

Install the required libraries with:

```bash
pip install networkx matplotlib
```

## Running the Program

Run the Python file:

```bash
python dijkstra.py
```

The program will first display the generated graph. It will then ask:

```text
Ορισε την αρχη του γραφου:
Ορισε το τελος του γραφου:
```

Enter the names of the nodes you want to use, for example:

```text
v1
v7
```

The shortest path will then be printed in the terminal and highlighted on the graph.

> **Note:** The node names are generated in the form `v1`, `v2`, ..., `v8`.

## Customizing the Graph

The graph can be easily changed by modifying a few values near the beginning of `dijkstra.py`.

### Number of edges

```python
for i in range(14):
```

The value `14` controls how many times the program attempts to generate an edge.

For example:

```python
for i in range(20):
```

will attempt to generate more edges.

Because duplicate edges and self-connections are rejected, the final number of edges can be lower than this value.

### Edge-weight range

```python
weight = random.randint(1, 7)
```

This controls the possible weights assigned to edges.

For example:

```python
weight = random.randint(1, 20)
```

would generate edge weights from 1 to 20.

### Node range

```python
x = random.randint(1, 8)
y = random.randint(1, 8)
```

These values control which nodes can appear in the generated graph.

With the current values, nodes are selected from:

```text
v1 to v8
```

For example, changing both `8`s to `12` allows nodes `v1` through `v12` to be selected:

```python
x = random.randint(1, 12)
y = random.randint(1, 12)
```

### Starting and ending nodes

The starting and ending nodes are entered when the program runs:

```python
self.start = input(...)
self.end = input(...)
```

### `dijkstra.py`

Contains the complete implementation, including:

- Random graph generation
- Graph visualization
- Edge-weight storage
- Dijkstra's algorithm
- Shortest-path reconstruction
- Highlighting of the shortest path

## Dijkstra Implementation

The `Dijkstra` class stores the graph, starting node, ending node, and the current shortest known distance to each node.

The algorithm runs through the graph and the shortest path is created.

The resulting path is then printed and used to highlight the corresponding edges in the graph.

## Visualization

The graph is drawn using `networkx` and `matplotlib`.

- Nodes represent vertices.
- Edges represent connections between vertices.
- Numbers on the edges represent their weights.
- The shortest path is highlighted in red.
