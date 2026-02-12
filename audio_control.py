from PySide6.QtWidgets import (
    QMessageBox,
    QPushButton, 
    QWidget,
    QVBoxLayout,
    )

class AudioControl():
    def __init__(self):
        super().__init__()

        # Audio buttons
        self.load_audio_button = QPushButton("Load Audio")
        self.load_audio_button.clicked.connect(self.load_audio_button_clicked)

        self.record_audio_button = QPushButton("Record Audio")
        self.record_audio_button.clicked.connect(self.record_audio_button_clicked)

        self.reset_audio_button = QPushButton("Reset Audio")
        self.reset_audio_button.clicked.connect(self.reset_audio_button_clicked)

        self.audio_buttons_layout = QVBoxLayout()
        self.audio_buttons_layout.addWidget(self.load_audio_button)
        self.audio_buttons_layout.addWidget(self.record_audio_button)
        self.audio_buttons_layout.addWidget(self.reset_audio_button)

        self.audio_buttons = QWidget()
        self.audio_buttons.setLayout(self.audio_buttons_layout)

    def load_audio_button_clicked(self):
        print("Load Audio button clicked")
        
    def record_audio_button_clicked(self):
        print("Record Audio button clicked")
    
    def reset_audio_button_clicked(self):
        print("Reset Audio button clicked")
        
        button = QMessageBox.question(
            self.audio_buttons,
            "Reset Audio",
            "Are you sure you want to reset the audio?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )

        if button == QMessageBox.StandardButton.Yes:
            print("Audio reset")
        else:
            print("Audio not reset")
