from PyQt6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, title: str):
        """Constructor.
        :param title: str
        """
        super().__init__()

        self.setWindowTitle(title)
