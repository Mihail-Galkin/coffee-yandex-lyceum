import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog

from dialog import Dialog


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()

        self.update_table()

        self.add.clicked.connect(self.add_click)
        self.edit.clicked.connect(self.edit_click)

    def add_click(self):
        dialog = Dialog(parent=self)
        value = dialog.exec()
        if value == QDialog.Accepted:
            print(1)
            res = dialog.get_result()
            self.cur.execute("INSERT INTO coffee (title, roasting, is_ground, description, price, "
                             "volume) VALUES (?, ?, ?, ?, ?, ?)", res)
            self.con.commit()
        self.update_table()

    def edit_click(self):
        r = self.tableWidget.currentRow()
        if r == -1:
            return
        id_ = self.tableWidget.item(r, 0).text()

        dialog = Dialog(parent=self)
        value = dialog.exec()
        if value == QDialog.Accepted:
            res = dialog.get_result()
            self.cur.execute("UPDATE coffee SET title = ?, roasting = ?, is_ground = ?, description = ?, price = ?, "
                             "volume = ? WHERE ID = ?", res + (id_,))
            self.con.commit()
        self.update_table()

    def update_table(self):
        res = self.cur.execute("SELECT * FROM coffee").fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Название', 'Обжарка', 'Молотый?', 'Вкус', 'Цена', 'Объем'])
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
