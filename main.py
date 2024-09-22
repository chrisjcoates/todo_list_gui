from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QCheckBox,
    QLabel,
)
from PyQt5.QtCore import Qt


class CreateTodo(QWidget):
    def __init__(self, name):
        super().__init__()

        self.name = name

        self.todo_widget = QWidget()

        self.todo_check = QCheckBox()
        self.todo_check.setChecked(False)
        self.todo_name = QLabel(self.name)
        self.edit_btn = QPushButton("edit")
        self.delete_btn = QPushButton("delete")

        self.todo_widget_layout = QHBoxLayout()
        self.todo_widget_layout.addWidget(self.todo_check)
        self.todo_widget_layout.addWidget(self.todo_name)
        self.todo_widget_layout.addWidget(self.edit_btn)
        self.todo_widget_layout.addWidget(self.delete_btn)

        self.setLayout(self.todo_widget_layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Todo List")
        self.resize(640, 600)

        todo_list = []

        self.create_layout_widgets()
        self.add_controls()

        self.todo_add_btn.clicked.connect(self.create_todo)

    def create_layout_widgets(self):
        # Create central widget
        self.central_widget = QWidget()
        self.central_widget_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_widget_layout)

        # Create main widget
        self.main_widget = QWidget()
        # self.main_widget.setStyleSheet("border: 1px solid white;")
        self.main_widget_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_widget_layout)
        self.central_widget_layout.addWidget(self.main_widget)

        # Create input widget
        self.input_widget = QWidget()
        self.input_widget.setMaximumHeight(50)
        # self.input_widget.setStyleSheet("border: 1px solid white;")
        self.input_widget_layout = QHBoxLayout()
        self.input_widget.setLayout(self.input_widget_layout)
        self.main_widget_layout.addWidget(self.input_widget)

        # Create filter widget
        self.filter_widget = QWidget()
        self.filter_widget.setMaximumHeight(40)
        # self.filter_widget.setStyleSheet("border: 1px solid white;")
        self.filter_widget_layout = QHBoxLayout()
        self.filter_widget.setLayout(self.filter_widget_layout)
        self.main_widget_layout.addWidget(self.filter_widget)

        # Create todo list widget
        self.list_widget = QWidget()
        self.list_widget_layout = QVBoxLayout()
        self.list_widget_layout.setAlignment(Qt.AlignTop)
        self.list_widget.setLayout(self.list_widget_layout)
        self.main_widget_layout.addWidget(self.list_widget)

        # Create count widget
        self.count_widget = QWidget()
        self.count_widget.setMaximumHeight(40)
        self.count_widget.setStyleSheet("border: 1px solid white;")
        self.count_widget_layout = QHBoxLayout()
        self.count_widget.setLayout(self.count_widget_layout)
        self.main_widget_layout.addWidget(self.count_widget)

        self.setCentralWidget(self.central_widget)

    def add_controls(self):

        # Create input controls
        self.todo_input = QLineEdit()
        self.todo_input.setMaximumHeight(70)
        self.todo_add_btn = QPushButton("add")
        self.input_widget_layout.addWidget(self.todo_input)
        self.input_widget_layout.addWidget(self.todo_add_btn)

        # Create filter controls
        self.active_filter_btn = QPushButton("Active")
        self.complete_filter_btn = QPushButton("Filter")
        self.filter_widget_layout.addWidget(self.active_filter_btn)
        self.filter_widget_layout.addWidget(self.complete_filter_btn)

    def create_todo(self):
        todo = CreateTodo("Make coffee")
        self.list_widget_layout.addWidget(todo)


app = QApplication([])
main_window = MainWindow()
main_window.show()
app.exec_()
