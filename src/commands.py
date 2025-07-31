import wikipedia
import webbrowser
import geocoder
import webbrowser
from tts_module import TextToSpeech

class CommandExecutor:
    def __init__(self):
        self.tts = TextToSpeech()
        wikipedia.set_lang('pt')

    def execute(self, command_data):
        command = command_data.get('command')
        
        if command == 'wikipedia':
            self._execute_wikipedia(command_data)
        elif command == 'youtube':
            self._execute_youtube(command_data)
        elif command == 'pharmacy':
            self._execute_pharmacy()
        elif command == 'help':
            self.tts.speak(command_data.get('message'))
        elif command == 'unknown':
            self.tts.speak(command_data.get('message'))

    def _execute_wikipedia(self, command_data):
        search_term = command_data.get('search_term')
        try:
            summary = wikipedia.summary(search_term, sentences=2)
            self.tts.speak(f"Segundo a Wikipedia: {summary}")
        except wikipedia.exceptions.DisambiguationError as e:
            self.tts.speak(f"Há várias opções para {search_term}. Por favor, seja mais específico.")
        except wikipedia.exceptions.PageError:
            self.tts.speak(f"Não encontrei informações sobre {search_term} na Wikipedia.")

    def _execute_youtube(self, command_data):
        search_term = command_data.get('search_term')
        self.tts.speak(f"Procurando por {search_term} no YouTube")
        webbrowser.open(f"https://www.youtube.com/results?search_query={search_term}")

    def _execute_pharmacy(self):
        self.tts.speak("Procurando farmácias próximas...")
        # Usando geocoder para obter a localização atual
        g = geocoder.ip('me')
        if g.latlng:
            lat, lng = g.latlng
            # Abre o Google Maps com farmácias próximas
            url = f"https://www.google.com/maps/search/farmácia/@{lat},{lng},15z"
            webbrowser.open(url)
            self.tts.speak("Encontrei algumas farmácias próximas e estou abrindo no seu navegador.")
        else:
            self.tts.speak("Não consegui determinar sua localização para encontrar farmácias próximas.")