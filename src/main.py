from stt_module import SpeechToText
from nlp_processor import CommandProcessor
from commands import CommandExecutor
from tts_module import TextToSpeech

class VirtualAssistant:
    def __init__(self):
        self.stt = SpeechToText()
        self.tts = TextToSpeech()
        self.processor = CommandProcessor()
        self.executor = CommandExecutor()
    
    def start(self):
        self.tts.speak("Olá! Sou seu assistente virtual. Como posso ajudar?")
        
        while True:
            text = self.stt.listen()
            
            if not text:
                continue
                
            if 'parar' in text or 'sair' in text or 'encerrar' in text:
                self.tts.speak("Até logo!")
                break
                
            try:
                command_data = self.processor.process(text)
                if isinstance(command_data, dict):
                    self.executor.execute(command_data)
                else:
                    self.tts.speak("Ocorreu um erro ao processar seu comando.")
            except Exception as e:
                print(f"Erro: {e}")
                self.tts.speak("Desculpe, ocorreu um erro ao processar seu pedido.")

if __name__ == "__main__":
    assistant = VirtualAssistant()
    assistant.start()