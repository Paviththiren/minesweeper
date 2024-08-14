import PyQt5.QtWidgets as qt
import sys  #The sys module is needed to processing command line arguments

app = qt.QApplication(sys.argv)

window = qt.QMainWindow()
window.setWindowTitle("Test Window")

button = qt.QPushButton()
button.setText("Press Me")

window.setCentralWidget(button)

window.show()


#Start the event loop
app.exec()