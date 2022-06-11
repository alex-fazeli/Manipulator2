import matplotlib.pyplot as plt
import numpy as np



def plot_mechanism(x_e, y_e, teta, L):

    for i in range(len(x_e)):

        plt.plot([0, L[0] * np.cos(teta[0, i]), L[0] * np.cos(teta[0, i])+L[1]*np.cos(teta[0, i]+teta[1, i]), L[0] * np.cos(teta[0, i]) + L[1]*np.cos(teta[0, i]+teta[1, i]) + L[2]*np.cos(teta[0, i]+teta[1, i]+teta[2, i])], [0, L[0] * np.sin(teta[0, i]), L[0] * np.sin(teta[0, i])+L[1]*np.sin(teta[0, i]+teta[1, i]), L[0] * np.sin(teta[0, i]) + L[1]*np.sin(teta[0, i]+teta[1, i]) + L[2]*np.sin(teta[0, i]+teta[1, i]+teta[2, i])])
        plt.pause(1)
    plt.plot(x_e, y_e)
    plt.show()