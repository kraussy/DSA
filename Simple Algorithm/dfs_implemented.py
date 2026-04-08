#finding the visited nodes
def dfs(matrix, node):
    visited = []

    def visit(n):
        if n in visited:
            return
        
        visited.append(n)

        for i, connected in enumerate(matrix[n]):
            if connected == 1:
                visit(i)

    visit(node)
    return visited

print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]], 3))
