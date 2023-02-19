from PyQt5.QtWidgets import QDialog

from UI.addEditCoffeeForm import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

    def get_result(self):
        return (self.title.text(), self.roasting.text(), int(self.is_ground.isChecked()),
                self.description.text(), self.price.value(), self.volume.value())
