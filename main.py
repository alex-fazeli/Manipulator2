import json
from robot_analyzer import end_effector_trajactory_creator


with open(r"C:\Users\amirf\PycharmProjects\Manipulator2\config.json") as f:
    config_param = json.load(f)
pi = config_param['initial_point']
pf = config_param['final_point']
N = config_param['N']

[X_ee, Y_ee, Phi_ee] = end_effector_trajactory_creator(pi, pf, N)


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
