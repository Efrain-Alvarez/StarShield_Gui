import sys
import sqlite3
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # labels
        title = qtw.QLabel("User Input")
        ship_ip_label = qtw.QLabel("Ship IP")
        ship_hull_label = qtw.QLabel("Ship Hull Number")
        tm_rate_label = qtw.QLabel("TM Rate")
        video_rate_label = qtw.QLabel("Video Rate")
        source_port_label = qtw.QLabel("Source Port")
        destination_port_label = qtw.QLabel("Destination Port")

        # inputs
        self.ship_ip_input = qtw.QLineEdit()
        self.ship_hull_input = qtw.QLineEdit()
        self.tm_rate_input = qtw.QLineEdit()
        self.video_rate_input = qtw.QLineEdit()
        self.source_port_input = qtw.QLineEdit()
        self.destination_port_input = qtw.QLineEdit()

        # buttons
        submit_button = qtw.QPushButton("Submit")
        #retrieve_button = qtw.QPushButton("Retrieve Data")

        # Main layout
        main_layout = qtw.QGridLayout()

        container1 = qtw.QWidget()
        container1_layout = qtw.QGridLayout()
        container1_layout.addWidget(ship_ip_label, 0, 0)
        container1_layout.addWidget(self.ship_ip_input, 0, 1)
        container1_layout.addWidget(ship_hull_label, 1, 0)
        container1_layout.addWidget(self.ship_hull_input, 1, 1)
        container1.setLayout(container1_layout)
        main_layout.addWidget(container1, 0, 0)
        container1.setStyleSheet("""
            QWidget {
                border: 2px solid black;
            }
        """)

        container2 = qtw.QWidget()
        container2_layout = qtw.QFormLayout()
        container2_layout.addRow("TM Rate", self.tm_rate_input)
        container2_layout.addRow("Video Rate", self.video_rate_input)
        container2_layout.addRow("Source Port", self.source_port_input)
        container2_layout.addRow("Destination Port", self.destination_port_input)
        container2.setLayout(container2_layout)
        main_layout.addWidget(container2, 0, 1)
        container2.setStyleSheet("""
            QWidget {
                border: 2px solid black;
            }
        """)

        main_layout.addWidget(submit_button, 1, 0, 1, 2)
        #main_layout.addWidget(retrieve_button, 2, 0, 1, 2)

        # Set layout
        self.setLayout(main_layout)
        self.setWindowTitle("User Input Form")

        # Button functionality
        submit_button.clicked.connect(self.on_submit)
        #retrieve_button.clicked.connect(self.retrieve_data)

        self.show()

    def on_submit(self):
        # Get the inputs from the form
        ship_ip = self.ship_ip_input.text()
        ship_hull = self.ship_hull_input.text()
        tm_rate = self.tm_rate_input.text()
        video_rate = self.video_rate_input.text()
        source_port = self.source_port_input.text()
        destination_port = self.destination_port_input.text()

        # Create a connection to SQLite (this creates the database if it doesn't exist)
        conn = sqlite3.connect('user_input.db')
        cursor = conn.cursor()

        cursor.execute('DROP TABLE IF EXISTS user_input')
        # Create a table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_input (
                ship_ip TEXT,
                ship_hull TEXT,
                tm_rate TEXT,
                video_rate TEXT,
                source_port TEXT,
                destination_port TEXT
            )
        ''')


        # Insert the user input data into the table
        cursor.execute('''
            INSERT INTO user_input (ship_ip, ship_hull, tm_rate, video_rate, source_port, destination_port)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (ship_ip, ship_hull, tm_rate, video_rate, source_port, destination_port))

        # Commit the transaction and close the connection
        conn.commit()
        conn.close()

        print("Form Submitted and data saved to database.")

    def retrieve_data(self):
        # Connect to the SQLite database
        conn = sqlite3.connect('user_input.db')
        cursor = conn.cursor()

        # Retrieve all rows from the 'user_input' table
        cursor.execute('SELECT * FROM user_input')
        rows = cursor.fetchall()

        # Close the connection
        conn.close()
        
        return rows

if __name__ == '__main__':
    # Application object
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    app.exec_()

    data = w.retrieve_data()
    print(data)
