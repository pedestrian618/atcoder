class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.color_sets = [set() for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def move(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        # If x and y are both roots, make y the new root
        if root_x == x and root_y == y and x != y:
            self.color_sets[root_y].update(self.color_sets[root_x])
            self.color_sets[root_x].clear()
            self.parent[root_x] = root_y
            return

        # If x is a root but y is not, make y the new root and move balls
        if root_x == x and root_y != y:
            self.parent[root_x] = root_y
            self.color_sets[root_y].update(self.color_sets[root_x])
            self.color_sets[root_x].clear()
            return

        # If x is not a root, no need to move balls, just update the parent
        if root_x != x:
            self.parent[x] = root_y


def main():
    N, Q = map(int, input().split())
    ball_colors = list(map(int, input().split()))

    uf = UnionFind(N)
    for i in range(N):
        uf.color_sets[i].add(ball_colors[i])

    for _ in range(Q):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        uf.move(a, b)
        print(len(uf.color_sets[uf.find(b)]))


if __name__ == "__main__":
    main()
