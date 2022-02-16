from PySide2.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QWidget, QHBoxLayout, QVBoxLayout, \
    QPushButton, QFrame
from PySide2.QtCore import QSize
from PySide2.QtGui import QFont
from functions import validity_test, create_random_card_number


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("bank card number")
        self.setFixedSize(QSize(600, 800))

        label_1 = QLabel("Validator :")
        label_1.setFont(QFont("Times font", 15))
        layout_1 = QVBoxLayout()
        layout_1.addWidget(label_1)

        label_2 = QLabel("Card number (16 digits) : ")
        self.line_edit_1 = QLineEdit()
        self.line_edit_1.setFixedSize(QSize(380, 40))
        self.line_edit_1.setTextMargins(100, 0, 0, 0)
        self.line_edit_1.setFont(QFont("Arial", 14))
        layout_2 = QHBoxLayout()
        layout_2.addWidget(label_2)
        layout_2.addWidget(self.line_edit_1)
        layout_2.setSpacing(5)

        button_1 = QPushButton("Validate")
        button_1.setFixedSize(QSize(400, 40))
        button_1.clicked.connect(self.push_validate)
        self.label_3 = QLabel()
        self.label_3.setStyleSheet("background-color: white; border: 1px inset gray;")
        self.label_3.setFrameShape(QFrame.Panel)
        self.label_3.setFrameShadow(QFrame.Sunken)
        self.label_3.setFixedSize(400, 50)
        self.label_3.setContentsMargins(80, 0, 30, 0)
        layout_3 = QVBoxLayout()
        layout_3.addWidget(button_1)
        layout_3.addWidget(self.label_3)
        layout_3.setContentsMargins(80, 0, 200, 0)

        label_4 = QLabel("Creator :")
        label_4.setFont(QFont("Times font", 15))
        layout_4 = QVBoxLayout()
        layout_4.addWidget(label_4)

        label_5 = QLabel("How many card numbers : ")
        self.line_edit_2 = QLineEdit()
        self.line_edit_2.setFixedSize(QSize(380, 40))
        self.line_edit_2.setTextMargins(100, 0, 0, 0)
        self.line_edit_2.setFont(QFont("Arial", 14))
        layout_5 = QHBoxLayout()
        layout_5.addWidget(label_5)
        layout_5.addWidget(self.line_edit_2)
        layout_5.setSpacing(5)

        label_6 = QLabel("inter 6 first digits if you want numbers for a special bank :")
        self.line_edit_3 = QLineEdit()
        self.line_edit_3.setFixedSize(QSize(360, 40))
        self.line_edit_3.setTextMargins(130, 0, 0, 0)
        self.line_edit_3.setFont(QFont("Arial", 20))
        layout_6 = QVBoxLayout()
        layout_6.addWidget(label_6)
        layout_6.addWidget(self.line_edit_3)
        layout_6.setSpacing(0)
        layout_6.setContentsMargins(100, 0, 30, 0)

        button_2 = QPushButton("Create file")
        button_2.setFixedSize(QSize(400, 50))
        button_2.clicked.connect(self.push_create_file)
        self.label_7 = QLabel()
        self.label_7.setStyleSheet("color : green;")
        layout_7 = QVBoxLayout()
        layout_7.addWidget(button_2)
        layout_7.addWidget(self.label_7)
        layout_7.setContentsMargins(76, 0, 90, 0)

        lay_out = QVBoxLayout()
        lay_out.addLayout(layout_1)
        lay_out.addLayout(layout_2)
        lay_out.addLayout(layout_3)
        lay_out.addLayout(layout_4)
        lay_out.addLayout(layout_5)
        lay_out.addLayout(layout_6)
        lay_out.addLayout(layout_7)
        lay_out.setSpacing(30)
        lay_out.setContentsMargins(20, 0, 20, 20)
        widget = QWidget()
        widget.setLayout(lay_out)
        self.setCentralWidget(widget)

    def push_validate(self):
        if self.line_edit_1.text().isdigit() == True and len(self.line_edit_1.text()) == 16:
            tested = validity_test(self.line_edit_1.text())
            self.label_3.setText(tested)

    def push_create_file(self):
        if self.line_edit_2.text().isdigit() == True and len(self.line_edit_2.text()) >= 1:
            f = open("nums.txt", "w")
            if self.line_edit_3.text().isdigit() == True and len(self.line_edit_3.text()) == 6:
                num_list = []
                while len(num_list) != int(self.line_edit_2.text()):
                    created_num = create_random_card_number(self.line_edit_3.text())
                    test_num = validity_test(created_num)
                    if test_num == "This bank card number is valid":
                        num_list.append(created_num)
                self.label_7.setText(" Ok !! card numbers are saved in a file with 'nums.txt' name .")
            else:
                num_list = []
                while len(num_list) != int(self.line_edit_2.text()):
                    created_num = create_random_card_number()
                    test_num = validity_test(created_num)
                    if test_num == "This bank card number is valid":
                        num_list.append(created_num)
                self.label_7.setText(" Ok !! card numbers are saved in a file with 'nums.txt' name .")
            f.write(str(num_list))


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
