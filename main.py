import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from containers import Ui_Form  # Make sure to replace this with the correct import based on your UI file

class MainWindow(qtw.QWidget):
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
        """Save the input values only when the submit button is clicked."""
        # Retrieve the input values from the UI
        self.ship_number = self.ui.Ship_number.text().strip()
        self.ship_ip = self.ui.Ship_ip.text().strip()
        self.tm_rate = self.ui.TM_rate.text().strip()
        self.video_rate = self.ui.Video_rate.text().strip()
        self.source_port = self.ui.Source_port.text().strip()
        self.des_port = self.ui.Des_port.text().strip()
        self.start_date = self.ui.Start_data.dateTime().toString()
        self.end_date = self.ui.End_date.dateTime().toString()

        # Validation of inputs
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
        
        # Save the data (this part only happens if all validations pass)
        print("Saved Data:")
        print(f"Ship Number: {self.ship_number}")
        print(f"Ship IP: {self.ship_ip}")
        print(f"TM Rate: {self.tm_rate}")
        print(f"Video Rate: {self.video_rate}")
        print(f"Source Port: {self.source_port}")
        print(f"Destination Port: {self.des_port}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")

    def show_error(self, title, message):
        """Display an error message box."""
        error_box = qtw.QMessageBox()
        error_box.setIcon(qtw.QMessageBox.Critical)
        error_box.setWindowTitle(title)
        error_box.setText(message)
        error_box.exec_()

    def is_valid_ip(self, ip):
        """Check if the IP address is valid."""
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
        """Check if the value is a valid number."""
        try:
            float(value)
            return True
        except ValueError:
            return False

    def is_valid_port(self, port):
        """Check if the port number is between 1 and 65535."""
        if not port.isdigit():
            return False
        port_num = int(port)
        return 1 <= port_num <= 65535

    def is_start_after_end(self):
        """Check if the start date is after the end date."""
        start_date = self.ui.Start_data.dateTime()
        end_date = self.ui.End_date.dateTime()
        return start_date > end_date

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
