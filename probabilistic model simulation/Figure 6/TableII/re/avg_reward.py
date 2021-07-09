import matplotlib.pyplot as plt
import os

def read_files(path, vector):
    lst = os.listdir(path)
    for fname in lst:
        if fname.endswith(".py") == 0:
            print(fname)
            with open(path+fname, "r") as rf:
                for i in range(1000):
                    rf.readline()
                number = float(rf.readline()[16:])
                vector.append(number)


if __name__ == "__main__":
    fixed_y = []

    adjust_r_01_y = []

    adjust_r_05_y = []

    adjust_r_07_y = []

    adjust_r_1_y = []

    adjust_r_2_y = []

    honest_y = []

    with open("avg_reward", "w") as wf:
        read_files("../../fixed/re/", fixed_y)
        wf.write("fixed: " + str(fixed_y) + "\n")
        read_files("../../adjust_r_4/re/", adjust_r_01_y)
        wf.write("r = 0.1: " + str(adjust_r_01_y) + "\n")
        read_files("../../adjust_r_3/re/", adjust_r_05_y)
        wf.write("r = 0.5: " + str(adjust_r_05_y) + "\n")
        read_files("../../adjust_r_5/re/", adjust_r_07_y)
        wf.write("r = 0.7: " + str(adjust_r_07_y) + "\n")
        read_files("../../adjust_r_1/re/", adjust_r_1_y)
        wf.write("r = 1: " + str(adjust_r_1_y) + "\n")
        read_files("../../adjust_r_2/re/", adjust_r_2_y)
        wf.write("r = 2: " + str(adjust_r_2_y) + "\n")
        read_files("../../honest/re/", honest_y)
        wf.write("honest: " + str(honest_y) + "\n")
