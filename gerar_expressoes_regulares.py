import PySimpleGUI as sg
from api import obter_regex

layout = [
    [sg.Text('Digite o que deseja criar:')],
    [sg.Multiline(key='-DESCRICAO-', size=(50, 10))],
    [sg.Button('Gerar Regex')],
    [sg.Text('', size=(50,1), key='-REGEX-')]
]

janela = sg.Window('Gerador de Regex', layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED:
        break
    if evento == 'Gerar Regex':
        descricao = valores['-DESCRICAO-']
        regex = obter_regex(descricao)
        janela['-REGEX-'].update(regex)

janela.close()