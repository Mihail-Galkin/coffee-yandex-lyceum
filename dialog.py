from PyQt5 import uic
from PyQt5.QtWidgets import QDialog


class Dialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        uic.loadUi("addEditCoffeeForm.ui", self)

    def get_result(self):
        return (self.title.text(), self.roasting.text(), int(self.is_ground.isChecked()),
                self.description.text(), self.price.value(), self.volume.value())
