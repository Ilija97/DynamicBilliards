import ProducePlots as pp
import PySimpleGUI as sg
import numpy as np

layout = [[sg.Text("Dynamical Billiards Generator")],
          [sg.Combo(['Square', 'Circle', 'Elipse','Triangle', 'Stadium', 'Bunimovich Billiard'],default_value='Square',key='billiard_table')],
          [sg.Text('Angle 1', size=(15, 1)), sg.InputText()],
          [sg.Text('Angle 2', size=(15, 1)), sg.InputText()],
          [sg.Text('Iterations', size=(15, 1)), sg.InputText()],
          [sg.Button("Generate")]]

# Create the window
window = sg.Window("Dynamical Billiards Generator", layout)

# Create an event loop
while True:
    event, values = window.read()
    print(values)
    # End program if user closes window or
    # presses the OK button
    values[0] = float(values[0]) * np.pi / 180
    values[1] = float(values[1]) * np.pi / 180
    values[2] = int(values[2])

    if event == "Generate":
        if values['billiard_table'] == 'Square':
            pp.printSquareBilliard(float(values[0]), float(values[1]), values[2])
        elif values['billiard_table'] == 'Triangle':
            pp.printTriangleBilliard(float(values[0]), float(values[1]), values[2])
        elif values['billiard_table'] == 'Circle':
            pp.printCircleBilliard(float(values[0]), float(values[1]), values[2])
        elif values['billiard_table'] == 'Elipse':
            pp.printElipseBilliard(float(values[0]), float(values[1]), values[2])
        elif values['billiard_table'] == 'Stadium':
            pp.printStadiumBilliard(float(values[0]), float(values[1]), values[2])
        elif values['billiard_table'] == 'Bunimovich Billiard':
            pp.printBunimovichBilliard(float(values[0]), float(values[1]), values[2])


    if event == sg.WIN_CLOSED:
        break

window.close()