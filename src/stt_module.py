import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self):
        """Ouve o microfone e converte fala em texto"""
        with self.microphone as source:
            print("Ajustando para ruído ambiente...")
            self.recognizer.adjust_for_ambient_noise(source)
            print("Diga algo...")
            audio = self.recognizer.listen(source)
            
            try:
                text = self.recognizer.recognize_google(audio, language='pt-BR')
                print(f"Você disse: {text}")
                return text.lower()
            except sr.UnknownValueError:
                print("Não entendi o que você disse")
                return ""
            except sr.RequestError:
                print("Serviço de reconhecimento de fala indisponível")
                return ""