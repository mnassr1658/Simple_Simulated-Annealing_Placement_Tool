import sys
from main import mainFunc
from PyQt5.QtWidgets import *

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

        self.filename = QLineEdit("file name, to re-enter another file name re-run the program")
        self.placement.layout.addWidget(self.filename)
        self.placement.setLayout(self.placement.layout)   
        
        self.submitButton = QPushButton("submit")
        self.submitMessage = QMessageBox()
        self.initialLengthmessage = QMessageBox()

        def funcOnClick():
            first_line, dict, hpl, initial = mainFunc(self.filename.text())

            #initialzing the 2D array (site)
            array = [['--' for x in range(first_line[1])] for y in range(first_line[0])] 

            #filling up the 2D array
            for i,z in dict.items():
                array[z[0]][z[1]] = i
            
         
            self.matrix = QTableWidget()
            self.matrix.setRowCount(first_line[0])
            self.matrix.setColumnCount(first_line[1])

            for i in range(0,len(array)):
                for j in range(0,len(array[0])):
                    row = array[i][j]
                    if (type(row) == type('-')):
                        self.matrix.setItem(i,j,QTableWidgetItem(row))
                    else:
                        num = "{:6.0f}".format(row)
                        self.matrix.setItem(i,j,QTableWidgetItem(num))

            self.placement.layout.addWidget(self.matrix)
            self.placement.setLayout(self.placement.layout)

            self.matrix.horizontalHeader().setStretchLastSection(True)
            self.matrix.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

            self.submitMessage.setText("Total wire Length = " + str(hpl))
            self.placement.layout.addWidget(self.submitMessage)
            self.submitMessage.exec_()
            self.initialLengthmessage.setText("Initial wire Length " + str(initial))
            self.placement.layout.addWidget(self.initialLengthmessage)
            self.initialLengthmessage.exec_()


        self.submitButton.clicked.connect(funcOnClick)
        self.placement.layout.addWidget(self.submitButton)
        self.placement.setLayout(self.placement.layout)

        self.layout.addWidget(self.bigboy)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())