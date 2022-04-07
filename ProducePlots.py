import os
import numpy as np
import BilliardClasses as BC
from matplotlib import pyplot as plt


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
# Folder to save the plots in
FIG_DIR = 'Plot images/'
FIG_DIR = os.path.join(CURRENT_DIR, FIG_DIR)
# Number of collisions to calculate


def printPositionPlot(board_list, title, start_angles):
    filename = "Billiard_table_%s.jpeg" % title
    filename = os.path.join(FIG_DIR, filename)
    title = "Billiard table - %s" % title
    # Generate basic plot properties
    fig, ax = plt.subplots(nrows=1, ncols=len(board_list), figsize=(15,7))
    fig.suptitle(title, fontsize=14, y=1)
    for i in range(len(board_list)):
        # Retrieve all relevant data
        collision_points = board_list[i].collision_points
        # Draw the board
        board_list[i].drawBoard(ax[i])
        # Draws the lines between collision points, i.e.
        ax[i].plot(collision_points[0], collision_points[1], color="b", linewidth=0.5)
        ax[i].set_xlabel(eval("start_angles[i]")/np.pi*180)
    fig.tight_layout()
    fig.savefig(filename, format='jpeg', pil_kwargs={'quality': 100}, dpi=1000)
    # plt.show()
    return plt.gcf()

def printSquareBilliard(start_angle_1, start_angle_2, num_collisions):
    print("generating square billiard plot")
    # Two billiard maps, same starting position but different launch angles
    square_start_position = np.array([[0.2], [0]])
    # Vertices of the square, going from
    square_vertices = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
    # Parameters of the square board class to use
    sq_para_1 = (num_collisions, square_vertices, square_start_position, start_angle_1)
    sq_para_2 = (num_collisions, square_vertices, square_start_position, start_angle_2)
    square_board_1 = BC.PolygonBilliardBoard(*sq_para_1)
    square_board_2 = BC.PolygonBilliardBoard(*sq_para_2)
    square_boards = [square_board_1, square_board_2]
    return printPositionPlot(square_boards, 'Square', [start_angle_1, start_angle_2])

def printTriangleBilliard(start_angle_1, start_angle_2, num_collisions):
    tri_start_position = np.zeros((2, 1))
    # Parameters of the triangle board class to use
    tri_para_1 = (num_collisions, 'triangle', tri_start_position, start_angle_1)
    tri_para_2 = (num_collisions, 'triangle', tri_start_position, start_angle_2)
    tri_board_1 = BC.PolygonBilliardBoard(*tri_para_1)
    tri_board_2 = BC.PolygonBilliardBoard(*tri_para_2)
    tri_boards = [tri_board_1, tri_board_2]
    return printPositionPlot(tri_boards, 'Triangle', [start_angle_1, start_angle_2])

def printCircleBilliard(start_angle_1, start_angle_2, num_collisions):
    circ_start_position = np.array([[0], [-1]])
    circ_para_1 = (num_collisions, (1, 1), circ_start_position, start_angle_1)
    circ_para_2 = (num_collisions, (1, 1), circ_start_position, start_angle_2)
    circ_board_1 = BC.EllipticalBilliardBoard(*circ_para_1)
    circ_board_2 = BC.EllipticalBilliardBoard(*circ_para_2)
    circ_boards = [circ_board_1, circ_board_2]
    return printPositionPlot(circ_boards, 'Circle', [start_angle_1, start_angle_2])

def printElipseBilliard(start_angle_1, start_angle_2, num_collisions):
    ellipse_start_position_1 = np.array([[-0.1], [0]])
    ellipse_start_position_2 = np.array([[-1.9], [0]])
    # Parameters of the ellipse board class to use
    ellipse_para_1 = (num_collisions, (2, 1), ellipse_start_position_1, start_angle_1)
    ellipse_para_2 = (num_collisions, (2, 1), ellipse_start_position_2, start_angle_2)
    ellipse_board_1 = BC.EllipticalBilliardBoard(*ellipse_para_1)
    ellipse_board_2 = BC.EllipticalBilliardBoard(*ellipse_para_2)
    ellipse_boards = [ellipse_board_1, ellipse_board_2]
    return printPositionPlot(ellipse_boards, 'Ellipse', [start_angle_1, start_angle_2])


def printHyperbolicBilliard(start_angle_1, start_angle_2, num_collisions):
    # Two billiard maps, same starting position but different launch angles
    hb_start = np.zeros((2, 1))
    # Parameters of the hyperbolic board class to use
    hb_para_1 = (num_collisions, (1, 1), hb_start, start_angle_1)
    hb_para_2 = (num_collisions, (1, 1), hb_start, start_angle_2)
    hb_board_1 = BC.HyperbolicBilliardBoard(*hb_para_1)
    hb_board_2 = BC.HyperbolicBilliardBoard(*hb_para_2)
    hb_boards = [hb_board_1, hb_board_2]
    return printPositionPlot(hb_boards, 'Hyperbolic', [start_angle_1, start_angle_2])


def printStadiumBilliard(start_angle_1, start_angle_2, num_collisions):
# Two billiard maps, same starting position but different launch angles
    stad_start = np.array([[0.5], [0]])
    # Parameters of the hyperbolic board class to use
    stad_para_1 = (num_collisions, (1, 1, 0.5), stad_start, start_angle_1)
    stad_para_2 = (num_collisions, (1, 1, 0.5), stad_start, start_angle_2)
    stad_board_1 = BC.StadiumBilliardBoard(*stad_para_1)
    stad_board_2 = BC.StadiumBilliardBoard(*stad_para_2)
    stad_boards = [stad_board_1, stad_board_2]
    return printPositionPlot(stad_boards, 'Stadium', [start_angle_1, start_angle_2])


def printBunimovichBilliard(start_angle_1, start_angle_2, num_collisions):
    # Two billiard maps, same starting position but different launch angles
    bunimovich_start = np.array([[0.5], [0]])
    # Parameters of the hyperbolic board class to use
    bunimovich_para_1 = (num_collisions, (1, 1, -0.25), bunimovich_start, start_angle_1)
    bunimovich_para_2 = (num_collisions, (1, 1, -0.25), bunimovich_start, start_angle_2)
    bunimovich_board_1 = BC.BunimovichBilliardBoard(*bunimovich_para_1)
    bunimovich_board_2 = BC.BunimovichBilliardBoard(*bunimovich_para_2)
    bunimovich_boards = [bunimovich_board_1, bunimovich_board_2]
    return printPositionPlot(bunimovich_boards, 'Bunimovich', [start_angle_1, start_angle_2])


def printLorentzGasBilliard(start_angle_1, start_angle_2, num_collisions):
    # Two billiard maps, same starting positions and different launch angles
    lg_start = np.array([[-1.2], [0]])
    # Parameters of the hyperbolic board class to use
    lg_para_1 = (num_collisions, None, lg_start, start_angle_1)
    lg_para_2 = (num_collisions, None, lg_start, start_angle_2)
    lg_board_1 = BC.LorentzGasBilliardBoard(*lg_para_1)
    lg_board_2 = BC.LorentzGasBilliardBoard(*lg_para_2)
    lg_boards = [lg_board_1, lg_board_2]
    return printPositionPlot(lg_boards, 'Lorentz Gas', [start_angle_1, start_angle_2])


def printHyperbolicLorentzGasBilliard(start_angle_1, start_angle_2, num_collisions):
    # Two billiard maps, same starting positions and different launch angles
    hlg_start = np.array([[0], [1.5]])
    # Parameters of the hyperbolic board class to use
    hlg_para_1 = (num_collisions, None, hlg_start, start_angle_1)
    hlg_para_2 = (num_collisions, None, hlg_start, start_angle_2)
    hlg_board_1 = BC.HyperbolicLorentzGasBilliardBoard(*hlg_para_1)
    hlg_board_2 = BC.HyperbolicLorentzGasBilliardBoard(*hlg_para_2)
    hlg_boards = [hlg_board_1, hlg_board_2]
    return printPositionPlot(hlg_boards, 'Hyperbolic Lorentz Gas', [start_angle_1, start_angle_2])
