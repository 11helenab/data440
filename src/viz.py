import matplotlib.pyplot as plt
import numpy as np
import os

PATH_FIGURES = 'figures'

#this file should contain code that makes figutes and does nothing else

def make_figure(data: np.ndarray, filename: str) -> None:
    '''
    Inputs: data a 2xn np array
    filenameL the file will be saved in figures folder
    '''
    full_filename = os.pathexists(PATH_FIGURES)
    os.mkdir(PATH_FIGURES)

    plt.figures(figsize=(6,6))
    plt.scatter(data[:,0], data[:, 1])
    plt.savefig(full_filename, bbox_inches='tight')
    plt.show()
    return None