class EdgeNode:
   def __init__(self,v1,v2,weight):
      self.vertex1 = v1
      self.vertex2 = v2
      self.weight = weight
   def edgeDetails(self):
      print(f"Edge: {self.vertex1}<-----{self.weight}----->{self.vertex2}")

class Graph:
   def __init__(self):
      self.vertices = {}
      self.edges = []
   
   def addEdge(self,edge,isdirected=False):
      if edge.vertex1 not in self.vertices:
         self.vertices[edge.vertex1] = []
      if edge.vertex2 not in self.vertices:
         self.vertices[edge.vertex2] = []

      self.vertices[edge.vertex1].append(edge.vertex2)
      if isdirected is False:
         self.vertices[edge.vertex2].append(edge.vertex1)
      self.edges.append(edge)

   def removeEdge(self,edge,isdirected=False):
      self.vertices[edge.vertex1].remove(edge.vertex2)
      if isdirected is False:
         self.vertices[edge.vertex2].remove(edge.vertex1)
      self.edges.remove(edge)

   def sortEdges(self):
      edgelist = self.edges[:]
      from operator import attrgetter
      edgelist.sort(key=attrgetter('weight'),reverse = False)
      return edgelist
   
   def kruskals(self):
      mst = Graph()
      edgelist = self.sortEdges()
      for edge in edgelist:
         print("Adding edge to MST : ",edge.edgeDetails())
         mst.addEdge(edge)
         set1 = set(mst.vertices[edge.vertex1])
         set2 = set(mst.vertices[edge.vertex2])
         print('-------------------')
         print(set1,set2)
         set3 = set1.intersection(set2)
         print(set3)

         if len(set3)!=0:
               mst.removeEdge(edge)
               print('Removing edge : ', edge.edgeDetails())
               print('-------------------')
      return mst
   
   def dfs(self,x):
      visited = set()
      temp_vertices = self.vertices
      temp_node = x
      self.dfs_2(visited,temp_vertices,temp_node)

   def dfs_2(self,visited,temp_vertices,temp_node):
      if temp_node not in visited:
         visited.add(temp_node)
         print(temp_node)
         for neighbour in temp_vertices[temp_node]:
            self.dfs_2(visited,temp_vertices,neighbour)
      
   def print_vertices(self):
      v_keys = self.vertices.keys()
      for key in v_keys:
         print(f"{key} : ",end = ' ')
         print(self.vertices[key])

   def print_edges(self):
      for i in self.edges:
         i.edgeDetails()



graph1 = Graph()
edge0 = EdgeNode(0,1,9)
edge1 = EdgeNode(0,2,75)
edge2 = EdgeNode(1,2,95)
edge3 = EdgeNode(1,3,19)
edge4 = EdgeNode(1,4,42)
edge5 = EdgeNode(2,3,51)
edge6 = EdgeNode(3,4,31)

edgeslist = [edge0,edge1,edge2,edge3,edge4,edge5,edge6]
for i in edgeslist:
   graph1.addEdge(i)
graph1.print_vertices()
graph1.print_edges()
graph1.kruskals()
graph1.dfs(0)