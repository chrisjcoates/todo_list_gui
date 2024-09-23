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
    QMessageBox,
)
from PyQt5.QtCore import Qt


class CreateTodo(QWidget):
    def __init__(self, name):
        super().__init__()

        self.name = name

        self.todo_widget = QWidget()

        self.todo_check = QCheckBox()
        self.todo_check.setMaximumWidth(40)
        self.todo_check.setChecked(False)
        self.todo_name = QLabel(self.name)
        self.todo_name.setAlignment(Qt.AlignLeft)
        self.edit_btn = QPushButton("edit")
        self.edit_btn.setMaximumWidth(60)
        self.delete_btn = QPushButton("delete")
        self.delete_btn.setMaximumWidth(60)

        self.todo_widget_layout = QHBoxLayout()
        self.todo_widget_layout.setContentsMargins(10, 0, 10, 0)
        self.todo_widget_layout.setSpacing(5)

        self.todo_widget_layout.addWidget(self.todo_check)
        self.todo_widget_layout.addWidget(self.todo_name)
        self.todo_widget_layout.addWidget(self.edit_btn)
        self.todo_widget_layout.addWidget(self.delete_btn)

        self.setLayout(self.todo_widget_layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Settings
        self.setWindowTitle("Todo List")
        self.resize(640, 600)

        # Todo lists
        self.active_todo_list = []
        self.complete_todo_list = []

        # Create layout and add controls
        self.create_layout_widgets()
        self.add_controls()

        # Add a todo
        self.todo_add_btn.clicked.connect(self.add_todo)
        self.complete_filter_btn.clicked.connect(self.complete_click)
        self.active_filter_btn.clicked.connect(self.active_click)

        # Complete a todo

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
        self.input_widget_layout = QHBoxLayout()
        self.input_widget.setLayout(self.input_widget_layout)
        self.main_widget_layout.addWidget(self.input_widget)

        # Create filter widget
        self.filter_widget = QWidget()
        self.filter_widget.setMaximumHeight(40)
        self.filter_widget_layout = QHBoxLayout()
        self.filter_widget.setLayout(self.filter_widget_layout)
        self.main_widget_layout.addWidget(self.filter_widget)

        # Create todo list widget (active)
        self.list_widget = QWidget()
        self.list_widget_layout = QVBoxLayout()
        self.list_widget_layout.setAlignment(Qt.AlignTop)
        self.list_widget.setLayout(self.list_widget_layout)
        self.main_widget_layout.addWidget(self.list_widget)

        # Create todo list widget (complete)
        self.completed_list_widget = QWidget()
        self.completed_list_widget_layout = QVBoxLayout()
        self.completed_list_widget_layout.setAlignment(Qt.AlignTop)
        self.completed_list_widget.setLayout(self.completed_list_widget_layout)
        self.main_widget_layout.addWidget(self.completed_list_widget)
        self.completed_list_widget.hide()

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
        self.complete_filter_btn = QPushButton("Complete")
        self.filter_widget_layout.addWidget(self.active_filter_btn)
        self.filter_widget_layout.addWidget(self.complete_filter_btn)

    def add_todo(self):
        if len(self.todo_input.text()) > 0:
            todo = CreateTodo(self.todo_input.text())

            todo.todo_check.stateChanged.connect(
                lambda state, t=todo: self.complete_todo(t, state)
            )

            self.active_todo_list.append(todo)
            self.list_widget_layout.addWidget(todo)
            self.todo_input.clear()
        else:
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Empty todo")
            msgbox.setText("You can't submit a blank todo")
            msgbox.setIcon(QMessageBox.Warning)
            msgbox.setStandardButtons(QMessageBox.Ok)
            msgbox.exec_()

    def complete_click(self):

        self.list_widget.hide()
        self.completed_list_widget.show()

        for todo in self.active_todo_list:
            todo.hide()

        for todo in self.complete_todo_list:
            todo.show()

    def active_click(self):
        self.list_widget.show()
        self.completed_list_widget.hide()

        for todo in self.complete_todo_list:
            todo.hide()

        for todo in self.active_todo_list:
            todo.show()

    def complete_todo(self, todo, state):
        if state == Qt.Checked:
            if todo in self.active_todo_list:
                todo.todo_name.setStyleSheet("text-decoration: line-through;")
                self.active_todo_list.remove(todo)
                self.list_widget_layout.removeWidget(todo)
                todo.hide()

                self.complete_todo_list.append(todo)
                self.completed_list_widget_layout.addWidget(todo)
        else:
            if todo in self.complete_todo_list:
                todo.todo_name.setStyleSheet("text-decoration: none;")
                self.complete_todo_list.remove(todo)
                self.completed_list_widget_layout.removeWidget(todo)
                todo.hide()

                self.active_todo_list.append(todo)
                self.list_widget_layout.addWidget(todo)


app = QApplication([])
main_window = MainWindow()
main_window.show()
app.exec_()
