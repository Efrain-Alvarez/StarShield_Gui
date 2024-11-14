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
        #Main layout
        main_layout = qtw.QGridLayout()

        container1 = qtw.QWidget()
        container1_layout = qtw.QGridLayout()
        container1_layout.addWidget(ship_ip_label,0,0)
        container1_layout.addWidget(ship_ip_input,0,1)
        container1_layout.addWidget(ship_hull_label,1,0)
        container1_layout.addWidget(ship_hull_input,1,1)
        container1.setLayout(container1_layout)
        main_layout.addWidget(container1,0,0)
        container1.setStyleSheet("""
            QWidget {
                border: 2px solid black;
            }
        """)
        
        container2 = qtw.QWidget()
        container2_layout = qtw.QFormLayout()
        container2_layout.addRow("tm rate", tm_rate_input)
        container2_layout.addRow("video rate", video_rate_input)
        container2.setLayout(container2_layout)
        main_layout.addWidget(container2,0,1)
        container2.setStyleSheet("""
            QWidget {
                border: 2px solid black;
            }
        """)

        #set layout
        self.setLayout(main_layout)
        self.show()


if __name__=='__main__':
    #application object
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
