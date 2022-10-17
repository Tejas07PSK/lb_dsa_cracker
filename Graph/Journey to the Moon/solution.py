class DisjointSet:
    def __init__ (self, n): self.parent = [[i, 1] for i in range(n)]
    def __find (self, node):
        curr_node = node
        while (self.parent[curr_node][0] != curr_node): curr_node = self.parent[curr_node][0]
        self.parent[node][0] = curr_node
        return curr_node, self.parent[curr_node][1]
    def union (self, node1, node2):
        parent1, size1 = self.__find(node1)
        parent2, size2 = self.__find(node2)
        if (parent1 != parent2):
            if (size1 < size2): parent2, parent1 = parent1, parent2
            self.parent[parent2][0] = parent1
            self.parent[parent1][1] += self.parent[parent2][1]

def journeyToMoon (n, astronaut):
    ds = DisjointSet(n)
    for astro_id1, astro_id2 in astronaut: ds.union(astro_id1, astro_id2)
    comp_size_counts = [ds.parent[i][1] for i in range(n) if (ds.parent[i][0] == i)]
    s, res = sum(comp_size_counts), 0
    for count in comp_size_counts:
        s -= count ; res += (count * s)
    return res
