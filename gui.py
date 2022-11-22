from PyQt5.QtWidgets import *
import sys
from main import mainFunc

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.left = 300
        self.top = 50
        self.width = 1300
        self.height = 1000
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.tab = bigwidget(self)
        self.setCentralWidget(self.tab)
        self.show()

class bigwidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.bigboy = QTabWidget()     

        self.placement = QWidget()
        self.bigboy.addTab(self.placement,"Placement")
        self.placement.layout = QVBoxLayout(self)

        self.filename = QLineEdit("file name")
        self.placement.layout.addWidget(self.filename)
        self.placement.setLayout(self.placement.layout)   
        
        self.submitButton = QPushButton("submit")

        def funcOnClick():
            first_line = mainFunc(self.filename.text())

            self.matrix = QTableWidget()
            self.matrix.setRowCount(first_line[0])
            self.matrix.setColumnCount(first_line[1])

            self.placement.layout.addWidget(self.matrix)
            self.placement.setLayout(self.placement.layout)


        self.submitButton.clicked.connect(funcOnClick)
        self.placement.layout.addWidget(self.submitButton)
        self.placement.setLayout(self.placement.layout)

        self.layout.addWidget(self.bigboy)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
