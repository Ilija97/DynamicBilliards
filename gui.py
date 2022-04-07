import ProducePlots as pp
import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def delete_fig_agg(fig_agg):
    fig_agg.get_tk_widget().forget()
    plt.close('all')


layout = [[sg.Text("Dynamical Billiards Generator")],
          [sg.Combo(['Square', 'Circle', 'Elipse','Triangle', 'Stadium', 'Bunimovich Billiard', 'Hyperbolic'], size=(14, 1)
                    ,default_value='Circle',key='billiard_table')],
          [sg.Text('Angle 1', size=(7, 1)), sg.InputText(size=(5, 1))],
          [sg.Text('Angle 2', size=(7, 1)), sg.InputText(size=(5, 1))],
          [sg.Text('Iterations', size=(7, 1)), sg.InputText(size=(5, 1))],
          [sg.Button("Generate")],
          [sg.Canvas(key='-CANVAS-')],
          ]

# Create the window
window = sg.Window("Dynamical Billiards Generator", layout, size=(1200, 700), finalize=True)

fig_agg = None
# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    values[0] = float(values[0]) * np.pi / 180
    values[1] = float(values[1]) * np.pi / 180
    values[2] = int(values[2]) + 1

    if event == "Generate":
        if fig_agg is not None:
            delete_fig_agg(fig_agg)

        if values['billiard_table'] == 'Square':
            pp.printSquareBilliard(float(values[0]), float(values[1]), values[2])

        elif values['billiard_table'] == 'Triangle':
            pp.printTriangleBilliard(float(values[0]), float(values[1]), values[2])

        elif values['billiard_table'] == 'Circle':
            fig_agg = draw_figure(window['-CANVAS-'].TKCanvas, pp.printCircleBilliard(float(values[0]), float(values[1]), values[2]))

        elif values['billiard_table'] == 'Elipse':
            pp.printElipseBilliard(float(values[0]), float(values[1]), values[2])
        elif values['billiard_table'] == 'Stadium':
            pp.printStadiumBilliard(float(values[0]), float(values[1]), values[2])
        elif values['billiard_table'] == 'Bunimovich Billiard':
            pp.printBunimovichBilliard(float(values[0]), float(values[1]), values[2])
        elif values['billiard_table'] == 'Hyperbolic':
            pp.printHyperbolicBilliard(float(values[0]), float(values[1]), values[2])


    if event == sg.WIN_CLOSED:
        break

window.close()