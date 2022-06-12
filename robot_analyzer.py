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

def end_effector_speed_calculator(pt_i, pt_f, T):
    speed_vector = np.zeros((3, 1))
    speed_vector[0] = (pt_f[0] - pt_i[0]) / T
    speed_vector[1] = (pt_f[1] - pt_i[1]) / T
    speed_vector[2] = (pt_f[2] - pt_i[2]) / T


    return speed_vector


def jacobian_calculator(Teta_1, Teta_2, Teta_3, L):


    a11 = -L[0]*np.sin(Teta_1) - L[1]*np.sin(Teta_1+Teta_2) - L[2]*np.sin(Teta_1+Teta_2+Teta_3)
    a12 = -L[1]*np.sin(Teta_1+Teta_2) - L[2]*np.sin(Teta_1+Teta_2+Teta_3)
    a13 = -L[2]*np.sin(Teta_1+Teta_2+Teta_3)

    a21 = L[0]*np.cos(Teta_1) + L[1]*np.cos(Teta_1+Teta_2) + L[2]*np.cos(Teta_1+Teta_2+Teta_3)
    a22 = L[1]*np.cos(Teta_1+Teta_2) + L[2]*np.cos(Teta_1+Teta_2+Teta_3)
    a23 = L[2]*np.cos(Teta_1+Teta_2+Teta_3)

    a31 = 1
    a32 = 1
    a33 = 1

    J = np.array([[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]])

    return J