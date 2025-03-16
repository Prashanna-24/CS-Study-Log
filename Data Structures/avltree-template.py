class Queue:
   class Node:
      def __init__(self, e, next=None):
         self.element = e
         self.next = next

   def __init__(self):
      self.front = None
      self.rear = None

   def isEmpty(self):
      return True if self.front == None else False

   def printQueue(self):
      temp = self.front
      while temp != None:
         print(temp.element.value)
         temp = temp.next

   def enqueue(self, e):
      node = self.Node(e)
      if self.rear == None:
         self.front = self.rear = node
         return
      self.rear.next = node
      self.rear = node

   def dequeue(self):
      if self.front == None:
         return None
      else:
         e = self.front.element
         self.front = self.front.next
         if self.front == None:
               self.rear = None
         return e


class BSTAVLTree_LinkedList:
   class Node:
      def __init__(self, e=None):
         self.value = e
         self.parent = None
         self.leftchild = None
         self.rightchild = None
         self.height = 0

   def __init__(self, typeoftree='BST'):
      self.root = None
      self.type = typeoftree  # default-'BST'-BinarySearchTree
      # 'AVL-AVLTree
      if self.type == 'BST':
         print("Binary Search Tree using Linked list is created..")
      if self.type == 'AVL':
         print("AVL Tree using Linked list is created..")

   def insert(self, e):
      if self.root is None:
         self.root = self.Node(e)
      else:
         self._insert_recursive(self.root, e)

      if self.type == 'AVL':
         print("AVL tree trinode structuring to balance")
      self.levelordertraversal(self.root)

   def _insert_recursive(self, node, e):
      if e < node.value:
         if node.leftchild is None:
               node.leftchild = self.Node(e)
         else:
               self._insert_recursive(node.leftchild, e)
      elif e > node.value:
         if node.rightchild is None:
               node.rightchild = self.Node(e)
         else:
               self._insert_recursive(node.rightchild, e)
      # Update height of the current node
      node.height = 1 + max(self._height(node.leftchild), self._height(node.rightchild))

   def _height(self, node):
      if node is None:
         return -1
      else:
         return node.height

   def delete(self, e):
      if self.root is None:
         return None
      else:
         self._delete_recursive(self.root, e)

   def _delete_recursive(self, node, e):
      if node is None:
         return node

      if e < node.value:
         node.leftchild = self._delete_recursive(node.leftchild, e)
      elif e > node.value:
         node.rightchild = self._delete_recursive(node.rightchild, e)
      else:
         # Case 1: Node with only one child or no child
         if node.leftchild is None:
               temp = node.rightchild
               node = None
               return temp
         elif node.rightchild is None:
               temp = node.leftchild
               node = None
               return temp

         # Case 2: Node with two children: Get the inorder successor (smallest in the right subtree)
         temp = self._min_value_node(node.rightchild)

         # Copy the inorder successor's content to this node
         node.value = temp.value

         # Delete the inorder successor
         node.rightchild = self._delete_recursive(node.rightchild, temp.value)

      if self.type == 'AVL':
         print("AVL tree trinode structuring to balance")
      return node

   def _min_value_node(self, node):
      current = node
      while current.leftchild is not None:
         current = current.leftchild
      return current

   def height(self, node):
      if node is None:
         return -1
      else:
         return node.height

   def depth(self, node):
      if node is None:
         return 0
      else:
         left_depth = self.depth(node.leftchild)
         right_depth = self.depth(node.rightchild)
         return max(left_depth, right_depth) + 1

   def balancedFactor(self, node):
      if node is None:
         return 0
      return self.height(node.leftchild) - self.height(node.rightchild)

   def inordertraversal(self, node):
      if node:
         self.inordertraversal(node.leftchild)
         print(node.value, end=" ")
         self.inordertraversal(node.rightchild)

   def preordertraversal(self, node):
      if node:
         print(node.value, end=" ")
         self.preordertraversal(node.leftchild)
         self.preordertraversal(node.rightchild)

   def postordertraversal(self, node):
      if node:
         self.postordertraversal(node.leftchild)
         self.postordertraversal(node.rightchild)
         print(node.value, end=" ")

   def levelordertraversal(self, node):
      q = Queue()
      elements = []
      if node == None:
         return None
      print("Level order traversal Enqueue")
      q.enqueue(node)

      while q.isEmpty() == False:
         node = q.dequeue()
         elements.append((node.value, node.height))
         if node.leftchild != None:
               q.enqueue(node.leftchild)
         if node.rightchild != None:
               q.enqueue(node.rightchild)
      print("LevelOrder:", elements)
      return

   def sorting(self, elements):
      return


class BSTAVLTree_Array:
   def __init__(self, typeoftree='BST', maxheight='5'):
      self.elements = []
      self.type = typeoftree  # default-'BST'-BinarySearchTree
      self.maxheight = maxheight
      # AVL-AVLTree
      if self.type == 'BST':
         print("Binary Search Tree using Array is created..")
      if self.type == 'AVL':
         print("AVL Tree using Array is created..")

   def insert(self, e):
      if self.type == 'AVL':
         print("AVL tree trinode structuring to balance")
      # Perform BST insertion in the array
      self.elements.append(e)

   def delete(self, e):
      if self.type == 'AVL':
         print("AVL tree trinode structuring to balance")
      # Perform BST deletion in the array if needed
      if e in self.elements:
         self.elements.remove(e)

   def getRoot(self):
      if len(self.elements) > 0:
         return self.elements[0]
      else:
         return None

   def isLeaf(self, node):
      # For array implementation, determine if the node is a leaf based on its position
      index = self.elements.index(node)
      left_child_index = 2 * index + 1
      right_child_index = 2 * index + 2
      if left_child_index >= len(self.elements) and right_child_index >= len(self.elements):
         return True
      else:
         return False

   def getMin(self, node):
      return min(self.elements)

   def getMax(self, node):
      return max(self.elements)

   def getMedian(self, node):
      sorted_elements = sorted(self.elements)
      length = len(sorted_elements)
      if length % 2 == 0:
         return (sorted_elements[length // 2 - 1] + sorted_elements[length // 2]) / 2
      else:
         return sorted_elements[length // 2]

   def height(self, node):
      # For array implementation, height is calculated based on the index of the last non-null element
      return self._calculate_height(0)

   def _calculate_height(self, index):
      if index >= len(self.elements) or self.elements[index] is None:
         return -1
      left_height = self._calculate_height(2 * index + 1)
      right_height = self._calculate_height(2 * index + 2)
      return max(left_height, right_height) + 1

   def depth(self, node):
      # For array implementation, depth is calculated based on the index of the element
      return self.elements.index(node)

   def balancedFactor(self, node):
      # For array implementation, balanced factor is not relevant
      return 0

   def inordertraversal(self, index):
      if index < len(self.elements) and self.elements[index] is not None:
         self.inordertraversal(2 * index + 1)
         print(self.elements[index], end=" ")
         self.inordertraversal(2 * index + 2)

   def preordertraversal(self, index):
      if index < len(self.elements) and self.elements[index] is not None:
         print(self.elements[index], end=" ")
         self.preordertraversal(2 * index + 1)
         self.preordertraversal(2 * index + 2)


# def main():
#     # Create a BST using linked list implementation
#     tree = BSTAVLTree_LinkedList("BST")

#     # Insert some elements into the tree
#     elements_to_insert = [50, 30, 70, 20, 40, 60, 80]
#     for element in elements_to_insert:
#         tree.insert(element)

#     print("Inorder Traversal:")
#     tree.inordertraversal(tree.root)
#     print("\nPreorder Traversal:")
#     tree.preordertraversal(tree.root)
#     print("\nPostorder Traversal:")
#     tree.postordertraversal(tree.root)
#     print("\nLevel Order Traversal:")
#     tree.levelordertraversal(tree.root)

#     # Delete an element from the tree
#     element_to_delete = 30
#     print("\nDeleting element:", element_to_delete)
#     tree.delete(element_to_delete)
   
#     print("Inorder Traversal after deletion:")
#     tree.inordertraversal(tree.root)
#     print("\nPreorder Traversal after deletion:")
#     tree.preordertraversal(tree.root)
#     print("\nPostorder Traversal after deletion:")
#     tree.postordertraversal(tree.root)
#     print("\nLevel Order Traversal after deletion:")
#     tree.levelordertraversal(tree.root)

# if _name_ == '_main_':
#     main()

   # Create a BST using array-based implementation
tree = BSTAVLTree_Array("BST")

# Insert some elements into the tree
elements_to_insert = [50, 30, 70, 20, 40, 60, 80]
for element in elements_to_insert:
   tree.insert(element)

print("Inorder Traversal:")
tree.inordertraversal(0)  # Passing index 0 as the root
print("\nPreorder Traversal:")
tree.preordertraversal(0)  # Passing index 0 as the root


# Delete an element from the tree
element_to_delete = 30
print("\nDeleting element:", element_to_delete)
tree.delete(element_to_delete)

print("Inorder Traversal after deletion:")
tree.inordertraversal(0)  # Passing index 0 as the root
print("\nPreorder Traversal after deletion:")
tree.preordertraversal(0)  # Passing index 0 as the root


# if _name_ == '_main_':
#    main()