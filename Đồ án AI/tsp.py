import time

class TSPBacktracking:
    def __init__(self, graph, city):
        self.graph = graph
        self.city = city
        self.n = len(graph)
        self.totalcost = []
        self.totalroute = []
        self.visited = [False] * self.n
        self.path = []
        self.shortest_path = float("inf")
        self.shortest_path_route = []
        self.mincost1 = float("inf")
        self.finalroute = []

    def tsp_backtracking(self, start):
        self.path = [start]
        self.visited[start] = True
        self.backtrack(start, 0, [start])

        for i in range(len(self.totalcost)):
            if self.totalcost[i] == self.mincost1:
                self.shortest_path = self.mincost1
                self.shortest_path_route.append(self.totalroute[i])

        for route in self.shortest_path_route:
            self.finalroute = [self.city[idx] for idx in route]
            print(f"Shortest path: {self.finalroute}, Cost: {self.shortest_path}")

        print(f"Total route: {len(self.totalroute)}")
        return self.shortest_path,self.finalroute

    def backtrack(self, current, cost, route):
        for i in range(self.n):
            if not self.visited[i] and self.graph[current][i] != 0 and cost + self.graph[current][i] < self.mincost1:
                self.path.append(i)
                self.visited[i] = True
                self.backtrack(i, cost + self.graph[current][i], route + [i])
                self.visited[i] = False
                self.path.pop()

        if len(self.path) == self.n:
            if self.graph[current][start] != 0:
                cost += self.graph[current][start]
                route += [start]
                self.totalcost.append(cost)
                self.totalroute.append(route)
                self.mincost1 = min(self.totalcost)
# Example usage:
if __name__ == "__main__":
    start_time = time.time()
    graph = [
        [0, 43, 76, 22, 87, 63, 72, 34, 54],
        [43, 0, 87, 34, 47, 88, 52, 67, 23],
        [76, 87, 0, 31, 64, 45, 22, 53, 49],
        [22, 34, 31, 0, 72, 54, 46, 88, 45],
        [87, 47, 64, 72, 0, 23, 34, 55, 61],
        [63, 88, 45, 54, 23, 0, 54, 36, 75],
        [72, 52, 22, 46, 34, 54, 0, 43, 64],
        [34, 67, 53, 88, 55, 36, 43, 0, 53],
        [54, 23, 49, 45, 61, 75, 64, 53, 0],
    ]
    # Gán tên thành phố theo thứ tự tương ứng:
    global city
    city = ["Arad","Sibiu","Bucharest","Fagaras","Zerind","Oradea","Craiova","Dobreta","Hirsova"]
    x = "Arad"
    idx = city.index(x)
    start = idx
    tsp = TSPBacktracking(graph,city)
    shortest_path = tsp.tsp_backtracking(start)
    print(tsp.finalroute)
    end_time = time.time()
    runtime = end_time - start_time
    print(f"Runtime: {runtime:.2f} seconds")