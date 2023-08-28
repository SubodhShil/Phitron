> # ```Bellman-Ford Algorithm```
Bellman ford is a graph shortest path algorithm that fixes limitations of greedy-based shortest path algorithm **Dijkstra**.

## Where **Dijkstra** algorithm fails
1. Can't predict shortest path if any negative weight cycle occurs (in an undirected graph).

![negative_cycle_in_graph](dijkstra_negative_cycle.jpg)

> The negative weight cycle enters into an infinite loop by decreasing values it's value continuously. This problem can be solved by tracking which nodes have already been visited, and let not revisit again. But, the fix can also lead to an incorrect or undesired shortest path.

## How Bellamn-Ford algorithm fixes problem
&nbsp;

> # ```Floyd Warshell Algorithm```
## Multi Source Shortest Path (MSSP)
Till now we've worked with graphs having a fixed source node and from that source we used to find shortest path to all other nodes or vertices. But, if we've to no fixed source node and said to find shortest path from each vertex. 

![bfs_dijkstra_bellman_time_complexity_MSSP](bfs_dijkstra_bellman_ford.png)

### When to use which algorithm
| **Criteria**         | **Algorithm**              |
| -------------------- | -------------------------- |
| Negative weight      | Floyd Warshell             |
| Only positive weight | Floyd Warshell or Dijkstra |
| No weight            | BFS                        |

Using Dijkstra and Bellman-Ford for finding multi source shortest path is not effecient. So, we have to use **Floyd Warshell** algorithm.

