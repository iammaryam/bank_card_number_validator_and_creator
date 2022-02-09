from PySide2.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QWidget, QHBoxLayout, QVBoxLayout, \
    QPushButton
from PySide2.QtCore import QSize
from card_number_validator import validity_test


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("card number validator")
        self.setFixedSize(QSize(650, 400))

        label = QLabel("card_number ( 16 digits ) :")
        self.line_edit = QLineEdit()
        self.line_edit.setFixedSize(QSize(350, 50))
        self.line_edit.setTextMargins(30, 0, 0, 0)

        layout_1 = QHBoxLayout()
        layout_1.setContentsMargins(10, 0, 100, 10)
        layout_1.addWidget(label)
        layout_1.addWidget(self.line_edit)

        button = QPushButton("SUBMIT")
        button.setFixedSize(QSize(300, 50))
        button.clicked.connect(self.test)

        layout_2 = QVBoxLayout()
        layout_2.addWidget(button)
        layout_2.setContentsMargins(180, 10, 10, 120)

        label_2 = QLabel()
        label_2.setText("RESULT: ")
        self.line_edit_2 = QLineEdit()
        self.line_edit_2.setFixedSize(QSize(450, 50))
        self.line_edit_2.setTextMargins(30, 0, 0, 0)

        layout_3 = QHBoxLayout()
        layout_3.addWidget(label_2)
        layout_3.addWidget(self.line_edit_2)
        layout_3.setContentsMargins(20, 0, 100, 20)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 50, 30, 10)
        layout.setSpacing(70)
        layout.addLayout(layout_1)
        layout.addLayout(layout_2)
        layout.addLayout(layout_3)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def test(self):
        tested = validity_test(self.line_edit.text())
        self.line_edit_2.setText(tested)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
