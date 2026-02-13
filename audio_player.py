from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QPushButton,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QSlider
    )

class AudioPlayer():
    def __init__(self):
        super().__init__()

        self.play_button = QPushButton("Play")
        self.play_button.pressed.connect(self.play_button_clicked)

        self.stop_button = QPushButton("Stop")
        self.stop_button.pressed.connect(self.stop_button_clicked)

        self.reset_button = QPushButton("Reset")
        self.reset_button.pressed.connect(self.reset_button_clicked)

        self.pause_button = QPushButton("Pause")
        self.pause_button.pressed.connect(self.pause_button_clicked)

        self.forward_button = QPushButton("Forward")
        self.forward_button.pressed.connect(self.forward_button_clicked)

        self.backward_button = QPushButton("Backward")
        self.backward_button.pressed.connect(self.backward_button_clicked)

        self.volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(100)
        self.volume_slider.valueChanged.connect(self.volume_slider_changed)

        self.top_layout = QHBoxLayout()
        self.top_layout.addWidget(self.play_button)
        self.top_layout.addWidget(self.stop_button)
        self.top_layout.addWidget(self.reset_button)
        self.top_layout.addWidget(self.pause_button)

        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.addWidget(self.forward_button)
        self.bottom_layout.addWidget(self.backward_button)
        self.bottom_layout.addWidget(self.volume_slider)

        self.audio_buttons_layout = QVBoxLayout()
        self.audio_buttons_layout.addLayout(self.top_layout)
        self.audio_buttons_layout.addLayout(self.bottom_layout) 

        self.audio_control_buttons = QWidget()
        self.audio_control_buttons.setLayout(self.audio_buttons_layout)

    def play_button_clicked(self):
        print("Play button clicked")
    
    def stop_button_clicked(self):
        print("Stop button clicked")
    
    def reset_button_clicked(self):
        print("Reset button clicked")

    def pause_button_clicked(self):
        print("Pause button clicked")

    def forward_button_clicked(self):
        print("Forward button clicked")

    def backward_button_clicked(self):
        print("Backward button clicked")

    def volume_slider_changed(self, value):
        print(f"Volume slider changed to {value}")      
