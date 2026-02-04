import sys 

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    )

from audio_control import AudioControl

class AMTMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AMT")

        self.setMinimumSize(QSize(1100, 800))

        # Audio buttons
        self.audio_control = AudioControl()
        self.setCentralWidget(self.audio_control.audio_buttons)

app = QApplication(sys.argv)

window = AMTMainWindow()
window.show()

app.exec()
