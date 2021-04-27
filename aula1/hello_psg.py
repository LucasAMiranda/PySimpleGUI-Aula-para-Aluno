import PySimpleGUI as sg

layout = [[sg.Text("hello from PySimpleGui")], [sg.Button("OK")]]

window = sg.Window("DEMO", layout)

while True:
    event, values = window.read()

    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
