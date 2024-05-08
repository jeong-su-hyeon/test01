import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget

class AddressBookApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("주소록")

        self.entries = {}

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        name_layout = QHBoxLayout()
        name_layout.addWidget(QLabel("이름: "))
        self.name_entry = QLineEdit()
        name_layout.addWidget(self.name_entry)

        phone_layout = QHBoxLayout()
        phone_layout.addWidget(QLabel("전화번호: "))
        self.phone_entry = QLineEdit()
        phone_layout.addWidget(self.phone_entry)

        layout.addLayout(name_layout)
        layout.addLayout(phone_layout)

        self.add_button = QPushButton("추가")
        self.add_button.clicked.connect(self.add_entry)
        layout.addWidget(self.add_button)

        self.listbox = QListWidget()
        layout.addWidget(self.listbox)

        self.delete_button = QPushButton("삭제")
        self.delete_button.clicked.connect(self.delete_entry)
        layout.addWidget(self.delete_button)

        self.setLayout(layout)

    def add_entry(self):
        name = self.name_entry.text()
        phone = self.phone_entry.text()

        if name and phone:
            self.entries[name] = phone
            self.listbox.addItem(f"{name}: {phone}")
            self.name_entry.clear()
            self.phone_entry.clear()

    def delete_entry(self):
        selected_item = self.listbox.currentItem()
        if selected_item:
            name = selected_item.text().split(":")[0].strip()
            del self.entries[name]
            self.listbox.takeItem(self.listbox.row(selected_item))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    address_book = AddressBookApp()
    address_book.show()
    sys.exit(app.exec_())
