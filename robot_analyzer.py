import numpy as np

def end_effector_trajactory_creator(pt_i, pt_f, N):

    X = np.linspace(pt_i[0], pt_f[0], num=N+1)
    Y = np.linspace(pt_i[1], pt_f[1], num=N+1)
    Phi = np.linspace(pt_i[2], pt_f[2], num=N+1)

    return X, Y, Phi