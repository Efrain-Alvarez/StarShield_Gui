import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from containers import Ui_Form

class MainWindow(qtw.QWidget):
    # Define a signal that carries all saved data as a dictionary
    data_saved = qtc.pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Build the UI from the XML
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        # Set background color
        self.setStyleSheet("background-color: white;")
        self.ui.groupBox.setStyleSheet("background-color:lightgrey;")
        self.ui.groupBox_2.setStyleSheet("background-color:lightgrey;")
        self.ui.groupBox_3.setStyleSheet("background-color:lightgrey;")
        self.ui.groupBox_4.setStyleSheet("background-color:lightgrey;")
        
        # Connect the Submit button to save_input method
        self.ui.pushButton.clicked.connect(self.save_input)
        
        # Show the window
        self.show()

        # Initialize instance variables to hold saved data
        self.ship_number = None
        self.ship_ip = None
        self.tm_rate = None
        self.video_rate = None
        self.source_port = None
        self.des_port = None
        self.start_date = None
        self.end_date = None

    def save_input(self):
        # Retrieve the input values from the UI when the submit button is clicked
        self.ship_number = self.ui.Ship_number.text().strip()
        self.ship_ip = self.ui.Ship_ip.text().strip()
        self.tm_rate = self.ui.TM_rate.text().strip()
        self.video_rate = self.ui.Video_rate.text().strip()
        self.source_port = self.ui.Source_port.text().strip()
        self.des_port = self.ui.Des_port.text().strip()
        self.start_date = self.ui.Start_data.dateTime().toString()
        self.end_date = self.ui.End_date.dateTime().toString()

        # Validation of inputs, checks if == to none or 0
        if not self.ship_number or not self.ship_ip or not self.tm_rate or not self.video_rate:
            self.show_error("Error", "Please fill in all the required fields.")
            return
        
        if not self.is_valid_ip(self.ship_ip):
            self.show_error("Invalid IP", "Please enter a valid IP address.")
            return
        
        if not self.is_valid_number(self.tm_rate) or not self.is_valid_number(self.video_rate):
            self.show_error("Invalid Rate", "Please enter valid numeric values for TM Rate and Video Rate.")
            return
        
        if not self.is_valid_port(self.source_port) or not self.is_valid_port(self.des_port):
            self.show_error("Invalid Port", "Please enter valid port numbers (between 1 and 65535).")
            return
        
        if self.is_start_after_end():
            self.show_error("Invalid Dates", "Start date must be before the end date.")
            return

        return {
            "ship_number": self.ship_number,
            "ship_ip": self.ship_ip,
            "tm_rate": self.tm_rate,
            "video_rate": self.video_rate,
            "source_port": self.source_port,
            "des_port": self.des_port,
            "start_date": self.start_date,
            "end_date": self.end_date
        }

    def show_error(self, title, message):
        # Displays error message
        error_box = qtw.QMessageBox()
        error_box.setIcon(qtw.QMessageBox.Critical)
        error_box.setWindowTitle(title)
        error_box.setText(message)
        error_box.exec_()

    def is_valid_ip(self, ip):
        # Check for a valid IP
        try:
            parts = ip.split(".")
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit() or not 0 <= int(part) <= 255:
                    return False
            return True
        except Exception:
            return False

    def is_valid_number(self, value):
        # Checks for valid numbers
        try:
            float(value)
            return True
        except ValueError:
            return False

    def is_valid_port(self, port):
        # Port number should be between 1 and 65535
        if not port.isdigit():
            return False
        port_num = int(port)
        return 1 <= port_num <= 65535

    def is_start_after_end(self):
        # Check if the start date is after the end date
        start_date = self.ui.Start_data.dateTime()
        end_date = self.ui.End_date.dateTime()
        return start_date > end_date

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    input_data = w.save_input()
    sys.exit(app.exec_())    
