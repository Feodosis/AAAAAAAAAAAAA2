# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QRadioButton
app = QApplication([])
win = QWidget()
win.setWindowTitle('Конкурс від Crazy People')
win.resize(400, 200)
question = QLabel(win)
question.setText('Якого року канал отримав золоту кнопку від Ютуб ?')
question.move(50, 10)

button1 = QRadioButton(win)
button1.setText('2005')
button1.move(100, 60)

button2 = QRadioButton(win)
button2.setText('2010')
button2.move(100, 110)

button3 = QRadioButton(win)
button3.setText('2015')
button3.move(200, 60)

button4 = QRadioButton(win)
button4.setText('2020')
button4.move(100, 90)

def show_win():
    win2 = QMessageBox()
    win2.setText('Правильно! Ви виграли Монако')
    win2.exec_()

button3.clicked.connect(show_win)
def show_lose():
    win2 = QMessageBox()
    win2.setText('Ні, в 2015 році. Ви виграли фірмовий плакат')
    win2.exec_()
button1.clicked.connect(show_lose)
button2.clicked.connect(show_lose)
button4.clicked.connect(show_lose)

win.show()
app.exec_()