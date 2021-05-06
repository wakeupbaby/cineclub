from movie import Movie
from PySide2 import QtWidgets, QtGui, QtCore

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cine Club")
        self.setup_ui()
        self.setup_connections()
        self.set_default_values()
        self.action()

    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)

        self.input_movie = QtWidgets.QLineEdit()
        self.list_widget = QtWidgets.QListWidget()
        self.btn_add = QtWidgets.QPushButton("Ajouter un film")
        self.btn_remomve = QtWidgets.QPushButton("Supprimer le(s) film(s)")

        self.layout.addWidget(self.input_movie)
        self.layout.addWidget(self.btn_add)
        self.layout.addWidget(self.list_widget)
        self.layout.addWidget(self.btn_remomve)
    
    def setup_connections(self):
        pass
    #     self.btn_add.activated.connect(add_to_movies())
    #     self.list_widget.activated.connect(self.compute)
    
    def set_default_values(self):
        pass
    # self.list_widgetFrom.setCurrentText(get_movies())

    def action(self):
        pass
    #     montant = self.le_montant.value()
    #     deviseFrom = self.cbb_devisesFrom.currentText()

    
app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
