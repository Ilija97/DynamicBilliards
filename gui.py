import ProducePlots as pp
import PySimpleGUI as sg

layout = [[sg.Text("Dynamical Billiards Generator")],
          [sg.Text('Angle 1')],
          [sg.Input()],
          [sg.Text('Angle 2')],
          [sg.Input()],
          [sg.Button("Generate")]]

# Create the window
window = sg.Window("Dynamical Billiards Generator", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Generate":
        pp.printSquareBilliard(1, 2)

    if event == sg.WIN_CLOSED:
        break

window.close()