# main.py
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QTextEdit, QPushButton, QVBoxLayout, 
    QHBoxLayout, QTabWidget
)
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from PyQt5.QtGui import QFont, QIcon, QMovie
from converter import text_to_morse, morse_to_text

class MorseApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text ↔ Morse Code Converter")
        self.setWindowIcon(QIcon('icon.png'))  
        self.setGeometry(100, 100, 600, 500)
        self.initUI()

    def initUI(self):
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        
        self.tabs.addTab(self.tab1, "Text to Morse")
        self.tabs.addTab(self.tab2, "Morse to Text")
        
        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText("Enter plain text here...")
        self.text_output = QTextEdit()
        self.text_output.setPlaceholderText("Morse code will appear here...")
        self.text_output.setReadOnly(True)
        self.convert_btn1 = QPushButton("Convert to Morse")
        self.convert_btn1.clicked.connect(self.convert_text_to_morse)
        
        layout1 = QVBoxLayout()
        layout1.addWidget(QLabel("Plain Text:"))
        layout1.addWidget(self.text_input)
        layout1.addWidget(self.convert_btn1)
        layout1.addWidget(QLabel("Morse Code:"))
        layout1.addWidget(self.text_output)
        self.tab1.setLayout(layout1)
        
        self.morse_input = QTextEdit()
        self.morse_input.setPlaceholderText("Enter Morse code here (use spaces and '/' for words)...")
        self.morse_output = QTextEdit()
        self.morse_output.setPlaceholderText("Plain text will appear here...")
        self.morse_output.setReadOnly(True)
        self.convert_btn2 = QPushButton("Convert to Text")
        self.convert_btn2.clicked.connect(self.convert_morse_to_text)
        
        layout2 = QVBoxLayout()
        layout2.addWidget(QLabel("Morse Code:"))
        layout2.addWidget(self.morse_input)
        layout2.addWidget(self.convert_btn2)
        layout2.addWidget(QLabel("Plain Text:"))
        layout2.addWidget(self.morse_output)
        self.tab2.setLayout(layout2)
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tabs)
        
        self.gif_label = QLabel(self)
        self.movie = QMovie("animation.gif")
        self.gif_label.setMovie(self.movie)
        self.movie.start()
        
        main_layout.addWidget(self.gif_label, alignment=Qt.AlignCenter)
        
        self.setLayout(main_layout)
        
        self.apply_stylesheet()
        
        self.animate_window()

    def apply_stylesheet(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #2E3440;
                color: #D8DEE9;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            QPushButton {
                background-color: #4C566A;
                border: none;
                padding: 10px;
                border-radius: 5px;
                color: #D8DEE9;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #88C0D0;
            }
            QTextEdit {
                background-color: #3B4252;
                border: 1px solid #4C566A;
                padding: 10px;
                border-radius: 5px;
                color: #ECEFF4;
                font-size: 14px;
            }
            QTabWidget::pane { /* The tab widget frame */
                border-top: 2px solid #4C566A;
            }
            QTabBar::tab {
                background: #4C566A;
                padding: 10px;
                border-radius: 4px;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background: #88C0D0;
                color: #2E3440;
            }
        """)

    def animate_window(self):
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(1000)
        self.animation.setStartValue(QRect(300, 300, 0, 0))
        self.animation.setEndValue(QRect(100, 100, 600, 500))
        self.animation.start()

    def convert_text_to_morse(self):
        text = self.text_input.toPlainText()
        if text.strip() == '':
            self.text_output.setPlainText("Please enter some text to convert.")
            return
        morse = text_to_morse(text)
        self.text_output.setPlainText(morse)

    def convert_morse_to_text(self):
        morse = self.morse_input.toPlainText()
        if morse.strip() == '':
            self.morse_output.setPlainText("Please enter some Morse code to convert.")
            return
        text = morse_to_text(morse)
        self.morse_output.setPlainText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MorseApp()
    window.show()
    sys.exit(app.exec_())