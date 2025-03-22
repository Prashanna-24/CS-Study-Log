class Graph:
   def init(self, vertices):
      self.vertices = vertices
      self.adj_list = {i: [] for i in range(vertices)}
      self.edges = []

   def add_edge(self, u, v, weight=1):
      self.adj_list[u].append((v, weight))
      self.adj_list[v].append((u, weight))
      self.edges.append((u, v, weight))

   def remove_edge(self, u, v):
      self.adj_list[u] = [(vert, w) for vert, w in self.adj_list[u] if vert != v]
      self.adj_list[v] = [(vert, w) for vert, w in self.adj_list[v] if vert != u]
      self.edges = [(x, y, w) for x, y, w in self.edges if not (x == u and y == v or x == v and y == u)]

   def remove_node(self, vertex):
      for i in range(self.vertices):
         self.adj_list[i] = [(vert, w) for vert, w in self.adj_list[i] if vert != vertex]
      self.adj_list.pop(vertex, None)
      self.edges = [(u, v, w) for u, v, w in self.edges if u != vertex and v != vertex]

      
   def bfs(self, start_vertex):
      visited = [False] * self.vertices
      queue = [start_vertex]
      result = []

      visited[start_vertex] = True

      while queue:
         vertex = queue.pop(0)
         result.append(vertex)

         for neighbour, _ in self.adj_list[vertex]:
               if not visited[neighbour]:
                  queue.append(neighbour)
                  visited[neighbour] = True

      return result

   def dfs(self, start_vertex):
      visited = [False] * self.vertices
      stack = [start_vertex]
      result = []

      while stack:
         vertex = stack.pop()
         if not visited[vertex]:
               result.append(vertex)
               visited[vertex] = True
               for neighbour, _ in self.adj_list[vertex]:
                  if not visited[neighbour]:
                     stack.append(neighbour)

      return result

   def kruskal(self):
      parent = list(range(self.vertices))
      
      def find(u):
         if parent[u] != u:
               parent[u] = find(parent[u])
         return parent[u]

      def union(u, v):
         root_u = find(u)
         root_v = find(v)
         if root_u != root_v:
               parent[root_u] = root_v

      mst_edges = []
      self.edges.sort(key=lambda x: x[2])

      for u, v, weight in self.edges:
         if find(u) != find(v):
               union(u, v)
               mst_edges.append((u, v, weight))

      return mst_edges

   def prim(self):
      from heapq import heappop, heappush
      min_heap = [(0, 0,0)]
      visited = [False] * self.vertices
      mst_edges = []
      total_cost = 0

      while min_heap:
         weight, u,v = heappop(min_heap)
         if visited[v]:
               continue
         visited[v] = True
         total_cost += weight
         mst_edges.append((u, v,weight))
         for vt, w in self.adj_list[v]:
               if not visited[vt]:
                  heappush(min_heap, (w,v,vt))
                  

      return mst_edges[1:]

   def dijkstra(self, start_vertex):
      from heapq import heappop, heappush
      distances = {vertex: float('inf') for vertex in range(self.vertices)}
      distances[start_vertex] = 0
      priority_queue = [(0, start_vertex)]
      
      while priority_queue:
         current_distance, current_vertex = heappop(priority_queue)

         if current_distance > distances[current_vertex]:
               continue

         for neighbor, weight in self.adj_list[current_vertex]:
               distance = current_distance + weight

               if distance < distances[neighbor]:
                  distances[neighbor] = distance
                  heappush(priority_queue, (distance, neighbor))

      return distances

   def graph_size(self):
      return self.vertices

   def get_neighbors(self, vertex):
      return self.adj_list[vertex]

   def print_graph(self):
      for vertex in self.adj_list:
         print(f"Vertex {vertex}: {self.adj_list[vertex]}")

def testGraph():
   vertices = 8
   graph = Graph(vertices)

   commands = [
      "AddEdge 0 1 4",
      "AddEdge 0 2 3",
      "AddEdge 1 2 1",
      "AddEdge 1 3 2",
      "AddEdge 2 3 4",
      "AddEdge 3 4 2",
      "AddEdge 4 5 6",
      "AddEdge 3 5 3",
      "AddEdge 5 6 1",
      "AddEdge 6 7 5",
      "AddEdge 5 7 2",
      "Print",
      "BFS 0",
      "DFS 0",
      "MST Kruskal",
      "MST Prim",
      "ShortestPath 0",
      "RemoveEdge 5 7",
      "Print",
      "RemoveNode 3",
      "Print",
      "End"
   ]

   for command in commands:
      operation = command.split()
      cmd_type = operation[0]

      if cmd_type == "AddEdge":
         u, v, w = int(operation[1]), int(operation[2]), int(operation[3])
         graph.add_edge(u, v, w)
         print(f"Edge added between {u} and {v} with weight {w}")
      
      elif cmd_type == "RemoveEdge":
         u, v = int(operation[1]), int(operation[2])
         graph.remove_edge(u, v)
         print(f"Edge removed between {u} and {v}")

      elif cmd_type == "RemoveNode":
         vertex = int(operation[1])
         graph.remove_node(vertex)
         print(f"Node {vertex} removed")

      elif cmd_type == "BFS":
         start_vertex = int(operation[1])
         result = graph.bfs(start_vertex)
         print(f"BFS from vertex {start_vertex}: {result}")

      elif cmd_type == "DFS":
         start_vertex = int(operation[1])
         result = graph.dfs(start_vertex)
         print(f"DFS from vertex {start_vertex}: {result}")

      elif cmd_type == "MST":
         algo = operation[1]
         if algo == "Kruskal":
               result = graph.kruskal()
               print(f"MST (Kruskal's): {result}")
         elif algo == "Prim":
               result = graph.prim()
               print(f"MST (Prim's): {result}")

      elif cmd_type == "ShortestPath":
         start_vertex = int(operation[1])
         result = graph.dijkstra(start_vertex)
         print(f"Shortest paths from vertex {start_vertex}: {result}")

      elif cmd_type == "Print":
         graph.print_graph()

def main():
   testGraph()

if name == "main":
   main()