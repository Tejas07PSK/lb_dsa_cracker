class DisjointSet:
    def __init__ (self, n): self.parent = [[i, 1] for i in range(n)]
    def find (self, node):
        curr_node = node
        while (self.parent[curr_node][0] != curr_node): curr_node = self.parent[curr_node][0]
        self.parent[node][0] = curr_node
        return curr_node, self.parent[curr_node][1]
    def union (self, node1, node2):
        parent1, size1, parent2, size2 = self.find(node1), self.find(node2)
        if (size1 < seize2): parent2, parent1 = parent1, parent2
        self.parent[parent2][0] = parent1
        self.parent[parent2][1] += self.parent[parent2][1]