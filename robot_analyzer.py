import numpy as np

def end_effector_trajactory_creator(pt_i, pt_f, N):

    X = np.linspace(pt_i[0], pt_f[0], num=N+1)
    Y = np.linspace(pt_i[1], pt_f[1], num=N+1)
    Phi = np.linspace(pt_i[2], pt_f[2], num=N+1)

    return X, Y, Phi

def joins_angles(x_e, y_e, phi_e, L):
    link_3_length = L[2]
    joint_2_x = x_e - link_3_length*np.cos(phi_e)
    joint_2_y = y_e - link_3_length * np.sin(phi_e)

    c2 = (np.power(joint_2_x, 2) + np.power(joint_2_y, 2) - L[0]**2-L[1]**2)/(2*L[0]*L[1])
    if np.any(abs(c2) > 1):
        raise ValueError('pose not achievable')
    s2 = np.sqrt(1-np.power(c2, 2))
    teta = np.zeros((3, np.shape(x_e)[0]))

    teta[1, :] = np.arctan2(s2, c2)

    k1 = L[0] + L[1] * c2
    k2 = L[1] * s2
    teta[0, :] = np.arctan2(joint_2_y, joint_2_x) - np.arctan2(k2, k1)
    teta[2, :] = phi_e - teta[0, :] - teta[1, :]


    return teta
