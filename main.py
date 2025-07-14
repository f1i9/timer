import sys
from PyQt5.QtWidgets import QShortcut, QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QKeySequence

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Timer")
        self.setGeometry(150, 1800, 400, 200)

        self.shortcut = QShortcut(QKeySequence('Ctrl+Q'), self)
        self.shortcut.activated.connect(self.close)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
