import pyttsx3

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        # Configurações de voz
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        self.engine.setProperty('rate', 150)

    def speak(self, text):
        """Converte texto em fala"""
        self.engine.say(text)
        self.engine.runAndWait()

    def save_to_file(self, text, filename):
        """Salva a fala em um arquivo de áudio"""
        self.engine.save_to_file(text, filename)
        self.engine.runAndWait()