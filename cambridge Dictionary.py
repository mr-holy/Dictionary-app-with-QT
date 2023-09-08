import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QMessageBox
import requests
from bs4 import BeautifulSoup
def kalameh(word):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    url = "https://dictionary.cambridge.org/dictionary/learner-english/%s"% word
    response = requests.get(url, headers=headers, timeout=10)  # Timeout set to 10 seconds
    try:
        soup = BeautifulSoup(response.text, "html.parser")
        definition_element = soup.find(class_="def ddef_d db")
        definition = definition_element.get_text()
        return definition
    except:
        return "error!"

class DictionaryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Dictionary App')

        self.input_word = QLineEdit(self)
        self.input_word.setPlaceholderText('Enter a word...')
        
        self.mean_button = QPushButton('Meaning', self)
        self.mean_button.clicked.connect(self.show_meaning)

        layout = QVBoxLayout()
        layout.addWidget(self.input_word)
        layout.addWidget(self.mean_button)

        self.setLayout(layout)

    def show_meaning(self):
        word = self.input_word.text()
        if word:
            try:
                meaning = kalameh(word)  # Call your function to get the meaning
                self.show_popup(f'Meaning of {word}', meaning)
            except Exception as e:
                self.show_popup('Error', str(e))
        else:
            self.show_popup('Error', 'Please enter a word.')

    def show_popup(self, title, message):
        popup = QMessageBox()
        popup.setWindowTitle(title)
        popup.setText(message)
        popup.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DictionaryApp()
    window.show()
    sys.exit(app.exec_())