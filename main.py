import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from random import choice

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
       
        # Taille de la fenêtere
        self.setFixedSize(300, 180)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Button layout en vertical

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        option_layout = QGridLayout()

        # Pour pouvoir pointer dessus : manipulable 
        self.password_generated = QLineEdit()

        # Button layout en horizontale

        button_layout = QHBoxLayout()

        main_layout.addLayout(option_layout)
        main_layout.addWidget(self.password_generated)
        main_layout.addLayout(button_layout)

        btn_quit = QPushButton("Quiter", self)
        btn_copy =QPushButton("Copier", self)
        btn_generate =QPushButton("Générer", self)
        button_layout.addWidget(btn_quit)
        button_layout.addWidget(btn_copy)
        button_layout.addWidget(btn_generate)

        # Texte
        self.txt_size = QLabel("Taile: 10")
        option_layout.addWidget(self.txt_size, 0, 0)

        self.option_size = QSlider(Qt.Horizontal)
        self.option_size.setMinimum(0)
        self.option_size.setMinimum(30)
        self.option_size.setMinimum(10)
        option_layout.addWidget(self.option_size, 1, 0)

        # Checkboxe

        self.option_lowercase = QCheckBox("Minuscules")
        option_layout.addWidget(self.option_lowercase, 0, 1)
        self.option_uppercase = QCheckBox("Majuscules")
        option_layout.addWidget(self.option_uppercase, 1, 1)
        self.option_numbers = QCheckBox("Chiffres")
        option_layout.addWidget(self.option_numbers, 0, 2)
        self.option_symbole = QCheckBox("Symboles")
        option_layout.addWidget(self.option_symbole, 1, 2)

        self.option_lowercase.setChecked(True)
        self.option_numbers.setChecked(True)

        # Affecter une action au clic
        btn_quit.clicked.connect(self.quit)
        btn_quit.clicked.connect(self.copy)

        self.option_size.valueChanged.connect(self.change_size)


    def quit(self):
        QApplication.quit()

    def copy(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.password_generated.text())

    def change_size(self):
        # récupérer la valeur => actualiser le texte
        value = self.option_size.value()
        self.txt_size.setText("Taille:" + str(value))

    def generated(self):
        size = self.option_size.value()
        has_lower = self.option_lowercase.isChecked()
        has_upper = self.option_uppercase.isChecked()
        has_number = self.option_numbers.isChecked()
        has_symbols = self.option_symbole.isChecked()

        letters = ""
        if has_lower:
            letters += "zaqwzsxedcrfvtgbyhnujikolpm"
        if has_upper:
            letters += "AQWZSXEDCRFVTGBYHNUJIKOLPM"
        if has_number:
            letters += "0123456789"
        if has_symbols:
            letters += "@%_&"
        
        password = ""
        for i in range(size):
            password += choice(letters)
        
        self.password_generated.setText(password)
        



app = QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle("Générateur de texte")
window.show()
app.exec()
