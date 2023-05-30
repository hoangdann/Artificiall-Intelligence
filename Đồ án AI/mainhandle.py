import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from main import Ui_MainWindow
from exp import ExpWindow
def tsp_backtracking(graph, start):
    n = len(graph)
    totalcost = []
    totalroute = []
    visited = [False] * n
    path = [start]
    visited[start] = True
    shortest_path = float("inf")
    shortest_path_route = []
    mincost1 = float("inf")
    def backtrack(current, cost, route):
        nonlocal shortest_path, shortest_path_route,totalcost, totalroute, mincost1
        for i in range(n):
            if not visited[i] and graph[current][i] != 0 and cost + graph[current][i] < mincost1:
                path.append(i)
                visited[i] = True
                backtrack(i, cost + graph[current][i], route + [i])
                visited[i] = False
                path.pop()  
        if len(path) == n:
            if graph[current][start] != 0:
                cost += graph[current][start]
                route += [start]
                totalcost.append(cost)
                totalroute.append(route)
                print(f"Path: {route}, Cost: {cost}")
                mincost1 = min(totalcost)
            return
    backtrack(start, 0, [start])
    for i in range(len(totalcost)):
      if totalcost[i] == mincost1:
            shortest_path = mincost1
            shortest_path_route.append(totalroute[i])
    first = []
    second = []
    first = shortest_path_route[0]
    second = shortest_path_route[1]  
    for i in range(len(first)):
          first[i] = city[first[i]]
    for i in range(len(second)):
        second[i] = city[second[i]]
    print(f"First path with minimum cost: {first}, Cost: {shortest_path}")
    print(f"Second path with minimum cost: {second}, Cost: {shortest_path}")
    print(f"Total route: {len(totalroute)}")  
    return shortest_path,first,second,shortest_path_route

class mainhandle(Ui_MainWindow):
    def __init__(self):
        self.setupUi(MainWindow)
        for x in city:
            self.comboBox.addItem(x)
        self.comboBox.activated.connect(self.setdata)
        self.pushButton.clicked.connect(self.load)
        
    def setdata(self):
        self.plainTextEdit.clear()
        x = self.comboBox.currentText()
        idx = city.index(x)
        start = idx
        shortest_path = tsp_backtracking(graph, start)
        self.plainTextEdit.insertPlainText(f"Tổng số quãng đường có chi phí tối ưu nhất: {str(len(shortest_path[3]))}\n")
        self.plainTextEdit.insertPlainText("Quãng đường thứ nhất: ")
        for x in shortest_path[1]:
            self.plainTextEdit.insertPlainText(f" - {str(x)}")
        self.plainTextEdit.appendPlainText("Quãng đường thứ hai: ")
        for x in shortest_path[2]:
            self.plainTextEdit.insertPlainText(f" - {str(x)}")
        self.plainTextEdit.appendPlainText(f"Tổng chi phí: {str(shortest_path[0])}")
    def load(self):
        explain = ExpWindow(MainWindow)


        
        
       
        
        
        


if __name__ == "__main__":
    import sys
    graph = [
        [0, 133, 232, 411, 524, 559, 342, 286, 284],
        [133, 0, 174, 231, 344, 419, 162, 106, 123],
        [232, 174, 0, 87, 200, 275, 191, 42, 221],
        [411, 231, 87, 0, 113, 179, 95, 58, 334],
        [524, 344, 200, 113, 0, 75, 229, 387, 518],
        [599, 419, 275, 179, 75, 0, 304, 462, 594],
        [342, 162, 191, 95, 229, 304, 0, 158, 349],
        [286, 106, 42, 58, 387, 462, 158, 0, 279],
        [284, 123, 221, 334, 518, 594, 349, 279, 0],
    ]
    city = ["Cà Mau","Sóc Trăng","Bến Tre","Tp Hồ Chí Minh","Bình Thuận","Lâm Đồng","Tây Ninh","Tiền Giang","An Giang"]
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mainhandle()
    MainWindow.show()
    sys.exit(app.exec_())