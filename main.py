

import random, pyperclip, sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt


LETTERS = "ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvwxyz0123456789$^*!@ç#/.?§_-&"

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Générer")
        self.button_copier = QtWidgets.QPushButton("Copier")
        self.text = QtWidgets.QLabel("", alignment=QtCore.Qt.AlignCenter)
        self.password_size = QtWidgets.QSlider(Qt.Horizontal, minimum=12, maximum=50)
        self.password_size_value = QtWidgets.QLabel(f"Taille: {str(self.password_size.value())} caractères.", alignment=QtCore.Qt.AlignCenter)

        # setStyleSheet =============
        
        self.button.setStyleSheet("""
            padding: 10px;
            background-color: green;
            color: white;

            font-size: 12px;
        """)

        self.button_copier.setStyleSheet("""
            padding: 10px;
            background-color: orange;
            color: white;

            font-size: 12px;
        """)

        self.text.setStyleSheet("""
            font-size: 16px;
            font-weight: 500;
        """)

        self.password_size_value.setStyleSheet("""
            font-size: 20px;
            font-weight: 200;
        """)
        

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout_bottom = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.password_size_value)
        self.layout.addWidget(self.password_size)
        self.layout.addWidget(self.text)
        self.layout.addLayout(self.layout_bottom)

        self.layout_bottom.addWidget(self.button)
        self.layout_bottom.addWidget(self.button_copier)

        self.button.clicked.connect(self.generate_password)
        self.button_copier.clicked.connect(self.copy_to_clipboard)
        self.password_size.valueChanged.connect(self.set_slider_text)

    def set_slider_text(self):
        self.password_size_value.setText(f"Taille: {str(self.password_size.value())} caractères.")
        

    def generate_password(self):
        password = self.mashup_letters()
        self.text.setText(password)
        # pyperclip.copy(password)

        # QtWidgets.QMessageBox.information(self, "Mot de passe copié", "Le mot de passe a été copié dans le presse-papier.")
    
    def copy_to_clipboard(self):
        pyperclip.copy(self.text.text())
        QtWidgets.QMessageBox.information(self, "Presse-papier", "Copié")


    def mashup_letters(self) -> str:
        generated_password = ""
        while len(generated_password) < self.password_size.value():
            generated_password += LETTERS[random.randint(0, len(LETTERS) - 1)]
        print(f"La valeur de password_length est: {self.password_size.value()} caractères.")
        return generated_password



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.setFixedSize(300, 200)
    widget.show()
    sys.exit(app.exec())

