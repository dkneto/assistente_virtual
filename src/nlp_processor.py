import re

class CommandProcessor:
    def __init__(self):
        self.commands = {
            'wikipedia': self.handle_wikipedia,
            'youtube': self.handle_youtube,
            'farmácia': self.handle_pharmacy,
            'farmacia': self.handle_pharmacy,
            'ajuda': self.handle_help
        }

    def process(self, text):
        """Processa o texto e identifica o comando"""
        for command in self.commands:
            if command in text:
                return self.commands[command](text)
        
        # Retorna um dicionário mesmo quando não reconhece o comando
        return {'command': 'unknown', 'message': "Desculpe, não entendi o comando. Diga 'ajuda' para ver as opções."}

    def handle_wikipedia(self, text):
        """Extrai o termo de pesquisa para Wikipedia"""
        search_term = re.sub(r'(pesquise|busque|procure|na wikipedia|wikipedia|sobre)', '', text, flags=re.IGNORECASE).strip()
        return {'command': 'wikipedia', 'search_term': search_term}

    def handle_youtube(self, text):
        """Extrai o termo de pesquisa para YouTube"""
        search_term = re.sub(r'(toque|abra|pesquise|no youtube|youtube|vídeo|video de)', '', text, flags=re.IGNORECASE).strip()
        return {'command': 'youtube', 'search_term': search_term}

    def handle_pharmacy(self, text):
        """Identifica o comando de farmácia"""
        return {'command': 'pharmacy'}

    def handle_help(self, text):
        """Retorna os comandos disponíveis"""
        help_text = """
        Comandos disponíveis:
        - Pesquise [termo] na Wikipedia
        - Abra [vídeo] no YouTube
        - Onde fica a farmácia mais próxima?
        """
        return {'command': 'help', 'message': help_text}