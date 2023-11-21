
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.diff_weight = [0] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            root = self.find(self.parent[x])
            self.diff_weight[x] += self.diff_weight[self.parent[x]]
            self.parent[x] = root
            return root

    def unite(self, x, y, w):
        w += self.diff_weight[x] - self.diff_weight[y]
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False

        if self.rank[x] < self.rank[y]:
            x, y = y, x
            w = -w

        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

        self.parent[y] = x
        self.diff_weight[y] = w
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def diff(self, x, y):
        return self.diff_weight[y] - self.diff_weight[x]


def good_set(N, Q):
    uf = UnionFind(N)
    good_elements = []

    for i in range(Q):
        a, b, d = map(int, input().split())
        a -= 1
        b -= 1
        if uf.same(a, b):
            if uf.diff(a, b) != d:
                continue
        else:
            uf.unite(a, b, d)
        good_elements.append(i + 1)

    return sorted(good_elements)


N, Q = map(int, input().split())
print(*good_set(N, Q))
