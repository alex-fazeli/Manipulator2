import json
from robot_analyzer import end_effector_trajactory_creator, joins_angles
from plot_utilities import plot_mechanism

with open(r"C:\Users\amirf\PycharmProjects\Manipulator2\config.json") as f:
    config_param = json.load(f)
pi = config_param['initial_point']
pf = config_param['final_point']
N = config_param['N']
L = config_param['L']

[x_e, y_e, phi_e] = end_effector_trajactory_creator(pi, pf, N)
teta = joins_angles(x_e, y_e, phi_e, L)

plot_mechanism(x_e, y_e, teta, L)





# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
