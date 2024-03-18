from typing import List, Optional
from collections import deque


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Node:
  def __init__(self, val=0, neighbors=None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []


class HelperFunctions:
  # Create the binary tree from the input list
  def createTree(self, input: List, index: int) -> TreeNode:
    if index < len(input):
      if input[index] is None:
        return None
      node = TreeNode(input[index])
      node.left = self.createTree(input, 2 * index + 1)
      node.right = self.createTree(input, 2 * index + 2)
      return node
    return None

  def printTree(self, root):
    if root:
      print(root.val)
      self.printTree(root.left)

  def generateGraph(self, adjacencyList: List[List]):
    nodesDict = {}
    # Create nodes and add them to the dictionary
    for i in range(len(adjacencyList)):
      node_val = i + 1  # Assuming node values are 1-based
      nodesDict[node_val] = Node(node_val)

    # Connect nodes based on the adjacency list
    for i in range(len(adjacencyList)):
      node_val = i + 1
      node = nodesDict[node_val]

      # Add neighbors to the node
      for neighbor_val in adjacencyList[i]:
        neighbor = nodesDict[neighbor_val]
        node.neighbors.append(neighbor)
    return nodesDict[1] if nodesDict else None

  def returnBackAdjacencyList(self, node, visited=None, adjacencyList=[]):
    if visited is None:
      visited = set()

    if node.val not in visited:
      visited.add(node.val)
      neighbors = [neighbor.val for neighbor in node.neighbors]
      adjacencyList.append(neighbors)

      for neighbor in node.neighbors:
        self.returnBackAdjacencyList(neighbor, visited, adjacencyList)
    return adjacencyList


class Solution:
  def invertTree(self, root: TreeNode) -> TreeNode:
    if not root:
      return None
    self.invertTree(root.left)
    self.invertTree(root.right)
    root.left, root.right = root.right, root.left
    return root

  def __init__(self):
    self.diameter = 0

  def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    self.depth(root)
    return self.diameter

  def depth(self, node):
    left = self.depth(node.left) if node.left else 0
    right = self.depth(node.right) if node.right else 0
    self.diameter = max(left + right, self.diameter)
    return max(left, right) + 1

  def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    if image[sr][sc] == color:
      return image
    self.fill(image, sr, sc, color, image[sr][sc])
    return image

  def fill(self, image, sr, sc, color, cur):
    if sr < 0 or sr > len(image) - 1 or sc < 0 or sc > len(image[0]) - 1:
      return
    if cur != image[sr][sc]:
      return
    image[sr][sc] = color
    self.fill(image, sr - 1, sc, color, cur)
    self.fill(image, sr + 1, sc, color, cur)
    self.fill(image, sr, sc - 1, color, cur)
    self.fill(image, sr, sc + 1, color, cur)
    return

  def buildAdjacentList(self, edgeList):
    adjacentMap = {}
    for v1, v2 in edgeList:
      if v2 not in adjacentMap:
        adjacentMap[v2] = []
      adjacentMap[v2].append(v1)
    return adjacentMap

  # v stands for vertex
  def topologicalBFS(self, numNodes, edgeList):
    adjacentMap = self.buildAdjacentList(edgeList)
    inDegrees = {i: 0 for i in range(numNodes)}
    for v1, v2 in edgeList:
      inDegrees[v1] += 1
    queue = []

    print(inDegrees)
    print(adjacentMap)

    for v in inDegrees:
      if inDegrees[v] == 0:
        queue.append(v)
    topologicalOrder, count = [], 0
    while queue:
      v = queue.pop(0)
      topologicalOrder.append(v)
      count += 1
      if v in adjacentMap:
        for des in adjacentMap[v]:
          inDegrees[des] -= 1
          if inDegrees[des] == 0:
            queue.append(des)
    if count != numNodes:
      return None
    else:
      return topologicalOrder

  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    return True if self.topologicalBFS(numCourses, prerequisites) else False

  def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    if not node:
      return node
    queue, map = deque(), {node: Node(node.val)}
    queue.append(node)

    while len(queue) > 0:
      cur = queue.popleft()
      for neighbor in cur.neighbors:
        if neighbor not in map:
          map[neighbor] = Node(neighbor.val)
          queue.append(neighbor)
        map[cur].neighbors.append(map[neighbor])
    return map[node]


class SecondSolution:
  # canFinish course schedule in DFS approach
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    map = {i: [] for i in range(numCourses)}
    for course, preReq in prerequisites:
      map[course].append(preReq)
    visiting = set()

    def dfs(course):
      if map[course] == []:
        return True
      if course in visiting:
        return False
      visiting.add(course)
      for preReq in map[course]:
        if not dfs(preReq):
          return False
      map[course] = []
      visiting.remove(course)
      return True
    for course in range(numCourses):
      if not dfs(course):
        return False
    return True


helper = HelperFunctions()
solution = Solution()
secondSolution = SecondSolution()


class Answer:
  def ans(self):

    # Tree
    # Input list representing the tree structure
    input_list = [4, 2, 7, 1, 3, 6, 9]
    root = helper.createTree(input_list, 0)
    print("Original Tree:")
    helper.printTree(root)
    # Invert the tree
    solution.invertTree(root)
    print("\nInverted Tree:")
    helper.printTree(root)

    input_list = [1, 2, 3, 4, 5]
    root = helper.createTree(input_list, 0)
    print("result")
    print(solution.diameterOfBinaryTree(root))

    # Graph
    image, sr, sc, color = [[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1,  1,  2
    print(solution.floodFill(image, sr, sc, color))

    numCourses, prerequisites = 2, [[0, 1]]
    print("\n" + f"{solution.canFinish(numCourses, prerequisites)}")
    print(secondSolution.canFinish(numCourses, prerequisites))

    node = [[2, 4], [1, 3], [2, 4], [1, 3]]
    input = helper.generateGraph(node)
    output = solution.cloneGraph(input)
    print(helper.returnBackAdjacencyList(output))


answer = Answer()
answer.ans()
