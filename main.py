import json
from robot_analyzer import end_effector_trajactory_creator, joins_angles, end_effector_speed_calculator, jacobian_calculator
from plot_utilities import plot_mechanism
import numpy as np
from numpy.linalg import inv


with open(r"C:\Users\amirf\PycharmProjects\Manipulator2\config.json") as f:
    config_param = json.load(f)
pi = config_param['initial_point']
pf = config_param['final_point']
N = config_param['N']
L = config_param['L']
time = config_param['time']

[x_e, y_e, phi_e] = end_effector_trajactory_creator(pi, pf, N)
teta = joins_angles(x_e, y_e, phi_e, L)

plot_mechanism(x_e, y_e, teta, L)

speed = end_effector_speed_calculator(pi, pf, time)

#teta_dot = np.zeros(np.shape(teta))
teta_dot = [[],[],[]]

for i in range(N+1):
    J = jacobian_calculator(teta[0, i], teta[1, i], teta[2, i], L)
    teta_dot = np.c_[teta_dot,  np.matmul(inv(J), speed)]

output = np.r_[teta, teta_dot]


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
