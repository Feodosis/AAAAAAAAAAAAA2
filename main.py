# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from random import randint
app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle("Визначник переможця")
my_win.move(100, 100)
my_win.resize(400, 200) #змінює розмір
button = QPushButton(my_win)
button.setText("Згенерувати")
button.move(140, 130)

text = QLabel(my_win)
text.setText("Натисніть, щоб дізнатись переможця")
text.move(70, 10)

winner = QLabel(my_win)
winner.setText("?")
winner.move(190, 70)

def show_winner():
    number = randint(1, 100)
    winner.setText(str(number))
    text.setText("Переможець:")
    text.move(190, 10)
button.clicked.connect(show_winner) #підключення функції


my_win.show()
app.exec_()


