import openai
import os

def obter_regex(descricao):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    try:
        resposta = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                # "system" é usado para definir o comportamento ou a personalidade do modelo para a sessão de chat.
                {'role': 'system', 'content': 'Você é um gerador de expressões regulares. Por favor, forneça apenas a expressão regular, sem explicações ou texto adicional.'},
                {'role': 'user', 'content': descricao}
            ]
        )
        return resposta.choices[0].message['content'].strip()
    except Exception as e:
        return f"Erro ao obter resposta da API: {e}"

if __name__ == '__main__':
    descricao = input('Digite a descrição para gerar a regex: ')
    print(obter_regex(descricao))