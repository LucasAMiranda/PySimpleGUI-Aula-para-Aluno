import PySimpleGUI as sg

layout = [[sg.Text('Entrar com um valor: '), sg.Input(key='-IN-')],
          [sg.Text('Saida aparece aqui ', size=(30, 1), key='-OUT-')],
          [sg.Button('OK'), sg.Button('Exit',  key='-OUT-')]]

Window = sg.Window('Title', layout)

# lógica

while True:
    event, value = Window.read()
    if event == '-OUT- ' or event == sg.WIN_CLOSED:
        break
    Window['-OUT-'].update(value['-IN-'])

Window.close()
