# Gerador de Regex com OpenAI ChatGPT

## Visão Geral

Este projeto é um gerador de expressões regulares (regex) que utiliza a API do ChatGPT da OpenAI para criar padrões regex com base em descrições fornecidas pelo usuário. A aplicação possui uma interface gráfica desenvolvida com PySimpleGUI.

## Funcionalidades

- **Entrada de Texto**: Permite que o usuário insira uma descrição detalhada do padrão regex desejado.
- **Geração de Regex**: Envia a descrição para a API do ChatGPT e retorna a expressão regular correspondente.
- **Interface Gráfica**: Utiliza PySimpleGUI para uma interação amigável com o usuário.

## Requisitos

Antes de executar o projeto, certifique-se de ter os seguintes requisitos:

- Python 3.x instalado.
- **Bibliotecas Python**:
    - `PySimpleGUI`
    - `openai`

**Chave da API OpenAI**: Você precisará de uma chave de API da OpenAI para utilizar o serviço. Defina sua chave da API como uma variável de ambiente chamada OPENAI_API_KEY.

## Instalação

Clone este repositório para sua máquina local:
```
git clone https://github.com/luizelias8/gerar-expressoes-regulares.git
cd gerar-expressoes-regulares
```

Instale os requisitos necessários:
```
pip install -r requirements.txt
```

## Uso

Execute o script:
```
python gerar_expressoes_regulares.py
```

## Exemplo

Se você deseja criar uma regex para validar e-mails, digite "criar uma regex para validar e-mail" na caixa de texto e clique em "Gerar Regex". A aplicação retornará a regex correspondente para validação de e-mail.

## Contribuição

Contribuições são bem-vindas!

## Autor

[Luiz Elias](https://github.com/luizelias8)