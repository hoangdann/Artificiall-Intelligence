from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
class ExpWindow(QtWidgets.QMainWindow):
    def set_bold_and_append_text(self, line1, line2):
        html_text = f"<br><b>{line1}</b><br>{line2}"
        self.textEdit.insertHtml(html_text)
    def tsp_backtracking(self, graph, start):
        n = len(graph)
        totalcost = []
        totalroute = []
        visited = [False] * n
        path = [start]
        visited[start] = True
        shortest_path = float("inf")
        shortest_path_route = []
        mincost1 = float("inf")
        remaining = list(set(range(n)) - set(path))
        startcity = city[0]
        def backtrack(current, cost, route, remaining):
            nonlocal shortest_path, shortest_path_route, totalcost, totalroute, mincost1


            for i in range(n):
                if not visited[i] and graph[current][i] != 0 and cost + graph[current][i] < mincost1:
                    current_city = city[i]  # Lấy tên thành phố từ danh sách city_names
                    path.append(i)
                    visited[i] = True
                    remaining.remove(i)
                    remain_city = [city[r] for r in remaining]
                    # Sử dụng current_city để hiển thị tên thành phố
                    self.textEdit.append(
                        f"Đoạn đường đang xét: {route + [current_city]}\nChi phí hiện tại: {cost + graph[current][i]}\nĐiểm đến tiếp theo: {remain_city}"
                    )

                    backtrack(i, cost + graph[current][i], route + [current_city], remaining)
                    visited[i] = False
                    path.pop()
                    remaining.append(i)

                if graph[current][i] != 0 and cost + graph[current][i] > mincost1 and not visited[i]:
                    self.set_bold_and_append_text(
                        f"Không tiếp tục xét đường đi này vì chi phí dự tính = {cost + graph[current][i]}",""
                    )
                    

            if len(path) == n:
                if graph[current][start] != 0:
                    cost += graph[current][start]
                    route += [startcity]
                    self.set_bold_and_append_text(f"Quãng đường hoàn thành: {route}",f"Chi phí: {cost}")
                    if cost <= mincost1:
                        totalcost.append(cost)
                    totalroute.append(route)
                    mincost1 = min(cost, mincost1)
                    self.set_bold_and_append_text(f"Chi phí tối ưu hiện tại: {mincost1}","")
                return

        backtrack(start, 0, [startcity], remaining)

        # Lưu trữ những quãng đường có giá trị min
        for i in range(len(totalcost)):
            if totalcost[i] == mincost1:
                shortest_path = mincost1
                shortest_path_route.append(totalroute[i])

        self.set_bold_and_append_text("Quãng đường thứ nhất: ","")
        for x in shortest_path_route[0]:
            self.textEdit.insertPlainText(f" - {str(x)}")
        self.set_bold_and_append_text("Quãng đường thứ hai: ","")
        for x in shortest_path_route[1]:
            self.textEdit.insertPlainText(f" - {str(x)}")
        self.set_bold_and_append_text(f"Chi phí tối ưu nhất: {mincost1}","")

        return shortest_path

        
    
    def __init__(self,MainWindow):
        super().__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(652, 717)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 631, 71))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 10, 631, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 30, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 631, 341))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("349560744_6234907603275158_8432164769230595225_n.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 440, 631, 191))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
  
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 652, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)





        graph = [
        [0, 12, 16, 17],
        [12, 0, 6, 25],
        [16, 6, 0, 14],
        [17, 25, 14, 0],
    
        ]
        global city
        city = ["Thạnh Mỹ Lợi","Trường Thọ","Tân Phú","Long Phước"]
        x = "Thạnh Mỹ Lợi"
        idx = city.index(x)
        start = idx
        shortest_path = self.tsp_backtracking(graph,start)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "GIẢI THÍCH CHI TIẾT THUẬT TOÁN BACKTRACKING"))
        self.label_2.setText(_translate("MainWindow", "ĐƯỢC SỬ DỤNG TRONG BÀI TOÁN TSP"))
        
    
 
        
        
        