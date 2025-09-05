import google.generativeai as genai


class Bot():
    """Cria um Bot especialista em desenhos"""
    def __init__(self):
        genai.configure(api_key="AIzaSyBP000QDKUVwZQLy98Zfbs6q0g5gwWbXy8")
        
        instrucao_sistema = """Você é uma designer de moda especialista em criação de coleções autorais, com foco em moda contemporânea e sustentabilidade.
Você possui 20 anos de experiência na indústria da moda.
Seu nome é Isadora Leclair. Você deve responder a todas as perguntas de forma profissional, criativa e detalhada, sempre com foco no universo do design de moda — incluindo processos criativos, pesquisa de tendências, modelagem, tecidos, construção de identidade de marca e inovação no vestuário.
Se o usuário perguntar sobre outro assunto, gentilmente redirecione a conversa de volta para o tema da moda, explicando que seu conhecimento é especializado exclusivamente nessa área."""
        
        
        self.model = genai.GenerativeModel(
            model_name='gemini-2.5-flash',
            system_instruction=instrucao_sistema)
        
        self.chat = self.model.start_chat()

    def enviar_mensagem(self, mensagem:str) -> str:
        """Função para responder as perguntas enviadas como paramêtro"""
        response = self.chat.send_message(mensagem)
        return response.text

#if que só execut se eu rodar o arquivo diretamente, caso eu importe essa parte nao sera executada, utilizado para testes

if __name__ == "__main__":
    robo = Bot()
    resposta = robo.enviar_mensagem("Me fale sobre medicina ")
    print(resposta)
    