from PySide6.QtWidgets import (
    QPushButton, 
    QWidget,
    QVBoxLayout,
    )

class AudioControl():
    def __init__(self):
        super().__init__()

        # Audio buttons
        self.load_audio_button = QPushButton("Load Audio")
        self.load_audio_button.clicked.connect(self.load_audio)

        self.record_audio_button = QPushButton("Record Audio")
        self.record_audio_button.clicked.connect(self.record_audio)

        self.audio_buttons_layout = QVBoxLayout()
        self.audio_buttons_layout.addWidget(self.load_audio_button)
        self.audio_buttons_layout.addWidget(self.record_audio_button)

        self.audio_buttons = QWidget()
        self.audio_buttons.setLayout(self.audio_buttons_layout)

    def load_audio(self):
        print("Load Audio button clicked")
        
    def record_audio(self):
        print("Record Audio button clicked")