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


layout = [[sg.Text("Dynamical Billiards Generator", font = ("Arial", 15))],
          [sg.Text("Ilija Gračanin, 2022", font = ("Arial", 8))],
          [sg.Frame(layout=[[sg.Combo(['Square', 'Circle', 'Semi circle', 'Elipse', 'Equilateral triangle', 'Right angled triangle', 'Hyperbolic'
                                       # 'Stadium', 'Bunimovich Billiard','Hyperbolic'
                                       ], size=(17, 1)
                                      , default_value='Circle', key='billiard_table')],
                            [sg.Text('Angle 1', size=(7, 1)), sg.InputText(size=(8, 1))],
                            [sg.Text('Angle 2', size=(7, 1)), sg.InputText(size=(8, 1))],
                            [sg.Text('Iterations', size=(7, 1)), sg.InputText(size=(8, 1))],
                            [sg.Button("Generate graph")]],
                    title='Graph Parameters', title_color='red', relief=sg.RELIEF_SUNKEN,
                    tooltip='Please fill in the parameters'),

           sg.Frame(layout=[[sg.Combo(['Square', 'Circle', 'Semi circle', 'Elipse', 'Elipse2', 'Equilateral triangle', 'Right angled triangle'], size=(17, 1)
                                      , default_value='Circle', key='billiard_table_anim')],
                            [sg.Text('Angle', size=(7, 1)), sg.InputText(size=(8, 1))],
                            [sg.Text('FPS', size=(7, 1)), sg.InputText(size=(8, 1))],
                            [sg.Text('Click Generate gif', size=(14, 1), key='OUTPUT')],
                            [sg.Button("Generate gif")]],
                    title='Gif parameters', title_color='red', relief=sg.RELIEF_SUNKEN,
                    tooltip='Please fill in the parameters'),

           sg.Frame(layout=[[sg.Text('The angle_1 is the initial angle for the billiard in the left figure, while the angle_2 is the '
                                     'initial angle for the billiard in the right figure.\n'
                                     'Angles are in degrees.\n'
                                     'Iterations is the number of collisions of the billiard ball with the boundary.')]],
                    title='Instructions', title_color='red', relief=sg.RELIEF_SUNKEN),
           ],
          [sg.Canvas(key='-CANVAS-')],
          ]

# Create the window
window = sg.Window("Dynamical Billiards Generator", layout, size=(1200, 800), finalize=True, resizable=True)

fig_agg = None
# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button

    if event == "Generate graph":

        values[0] = float(values[0]) * np.pi / 180
        values[1] = float(values[1]) * np.pi / 180
        values[2] = int(values[2]) + 1

        if fig_agg is not None:
            delete_fig_agg(fig_agg)

        if values['billiard_table'] == 'Square':
            fig_agg = draw_figure(window['-CANVAS-'].TKCanvas,
                                  pp.printSquareBilliard(float(values[0]), float(values[1]), values[2]))

        elif values['billiard_table'] == 'Equilateral triangle':
            fig_agg = draw_figure(window['-CANVAS-'].TKCanvas,
                                  pp.printTriangleBilliard(float(values[0]), float(values[1]), values[2]))

        elif values['billiard_table'] == 'Right angled triangle':
            fig_agg = draw_figure(window['-CANVAS-'].TKCanvas,
                                  pp.printRightAngleTriangleBilliard(float(values[0]), float(values[1]), values[2]))

        elif values['billiard_table'] == 'Circle':
            fig_agg = draw_figure(window['-CANVAS-'].TKCanvas,
                                  pp.printCircleBilliard(float(values[0]), float(values[1]), values[2]))

        elif values['billiard_table'] == 'Semi circle':
            fig_agg = draw_figure(window['-CANVAS-'].TKCanvas,
                                  pp.printSemiCircle(float(values[0]), float(values[1]), values[2]))

        elif values['billiard_table'] == 'Elipse':
            fig_agg = draw_figure(window['-CANVAS-'].TKCanvas,
                                  pp.printElipseBilliard(float(values[0]), float(values[1]), values[2]))

        # elif values['billiard_table'] == 'Stadium':
        #     fig_agg = draw_figure(window['-CANVAS-'].TKCanvas,
        #                           pp.printStadiumBilliard(float(values[0]), float(values[1]), values[2]))

        # elif values['billiard_table'] == 'Bunimovich Billiard':
        #     fig_agg = draw_figure(window['-CANVAS-'].TKCanvas,
        #                           pp.printBunimovichBilliard(float(values[0]), float(values[1]), values[2]))
        #
        elif values['billiard_table'] == 'Hyperbolic':
            fig_agg = draw_figure(window['-CANVAS-'].TKCanvas,
                                  pp.printHyperbolicBilliard(float(values[0]), float(values[1]), values[2]))

    if event == "Generate gif":
        anim_angle = float(values[3]) * np.pi / 180
        fps = int(values[4])

        if values['billiard_table_anim'] == 'Square':
            if pp.animateSquareBilliard(anim_angle, fps=fps) == 0:
                window['OUTPUT'].update(value="Gif exported")

        elif values['billiard_table_anim'] == 'Equilateral triangle':
            if pp.animateTriangleBilliard(anim_angle, fps=fps) == 0:
                window['OUTPUT'].update(value="Gif exported")

        elif values['billiard_table_anim'] == 'Right angled triangle':
            if pp.animateRightAnlgeTriangleBilliard(anim_angle, fps=fps) == 0:
                window['OUTPUT'].update(value="Gif exported")

        elif values['billiard_table_anim'] == 'Circle':
            if pp.animateCircleBilliard(anim_angle, fps=fps) == 0:
                window['OUTPUT'].update(value="Gif exported")

        elif values['billiard_table_anim'] == 'Semi circle':
            if pp.animateSemiCircleBilliard(anim_angle, fps=fps) == 0:
                window['OUTPUT'].update(value="Gif exported")

        elif values['billiard_table_anim'] == 'Elipse':
            if pp.animateElipseBilliard(anim_angle, fps=fps) == 0:
                window['OUTPUT'].update(value="Gif exported")

        elif values['billiard_table_anim'] == 'Elipse2':
            if pp.animateElipseBilliard2(anim_angle, fps=fps) == 0:
                window['OUTPUT'].update(value="Gif exported")

    if event == sg.WIN_CLOSED:
        break

window.close()
