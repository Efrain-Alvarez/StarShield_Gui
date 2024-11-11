import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from containers import Ui_Form

class MainWindow(qtw.QWidget):
    #parameters(instace of object, list of positional arguments,dictionary of keyword arguments )
    def __init__(self, *args, **kwargs):
        #refernce to parent function: QWidget, passing all the arguments that were passed to the parent function. 
        super().__init__(*args, **kwargs)
        #labels
        title = qtw.QLabel("User Input")
        ship_ip_label = qtw.QLabel("Ship IP")
        ship_hull_label = qtw.QLabel("Ship Hull Number")
        tm_rate_label = qtw.QLabel("TM Rate")
        video_rate_label = qtw.QLabel("Video Rate")
        source_port_label = qtw.QLabel("Source Port")
        destination_port_label = qtw.QLabel("Destination Port")
        #inputs
        ship_ip_input = qtw.QLineEdit()
        ship_hull_input = qtw.QLineEdit()
        tm_rate_input = qtw.QLineEdit()
        video_rate_input = qtw.QLineEdit()
        source_port_input = qtw.QLineEdit()
        destination_port_input = qtw.QLineEdit()
        #buttons
        submit_button = qtw.QPushButton("Submit")
        #layout
        
        self.show()


if __name__=='__main__':
    #application object
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())