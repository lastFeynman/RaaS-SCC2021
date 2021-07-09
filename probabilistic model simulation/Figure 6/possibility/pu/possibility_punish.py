import matplotlib.pyplot as plt
import os

def read_files(path, vector):
    lst = os.listdir(path)
    for fname in lst:
        if fname.endswith(".py") == 0:
            print(fname)
            with open(path+fname, "r") as rf:
                for i in range(1001):
                    rf.readline()
                number = float(rf.readline()[12:])
                vector.append(number)


if __name__ == "__main__":
    fixed_x = [0.000, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009]
    fixed_y = []
    
    adjust_r_01_x = [0.000, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009]
    adjust_r_01_y = []
    
    adjust_r_05_x = [0.000, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009]
    adjust_r_05_y = []
    
    adjust_r_07_x = [0.000, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009]
    adjust_r_07_y = []
    
    adjust_r_1_x = [0.000, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009]
    adjust_r_1_y = []
    
    adjust_r_2_x = [0.000, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009]
    adjust_r_2_y = []

    with open("possibility", "w") as wf:
        read_files("../../fixed/pu/", fixed_y)
        wf.write("fixed: " + str(fixed_y) + "\n")
        read_files("../../adjust_r_4/pu/", adjust_r_01_y)
        wf.write("r = 0.1: " + str(adjust_r_01_y) + "\n")
        read_files("../../adjust_r_3/pu/", adjust_r_05_y)
        wf.write("r = 0.5: " + str(adjust_r_05_y) + "\n")
        read_files("../../adjust_r_5/pu/", adjust_r_07_y)
        wf.write("r = 0.7: " + str(adjust_r_07_y) + "\n")
        read_files("../../adjust_r_1/pu/", adjust_r_1_y)
        wf.write("r = 1: " + str(adjust_r_1_y) + "\n")
        read_files("../../adjust_r_2/pu/", adjust_r_2_y)
        wf.write("r = 2: " + str(adjust_r_2_y) + "\n")
    
    plt.xlabel("k_pu")
    plt.ylabel("possibility")
    
    plt.plot(adjust_r_01_x, adjust_r_01_y, color="red", alpha=1, label="driver profile r = 0.1")
    plt.plot(adjust_r_05_x, adjust_r_05_y, color="yellow", alpha=1, label="driver profile r = 0.5")
    plt.plot(adjust_r_07_x, adjust_r_07_y, color="purple", alpha=1, label="driver profile r = 0.7")
    plt.plot(adjust_r_1_x, adjust_r_1_y, color="grey", alpha=1, label="driver profile r = 1")
    plt.plot(adjust_r_2_x, adjust_r_2_y, color="orange", alpha=1, label="driver profile r = 2")
    plt.plot(fixed_x, fixed_y, color="green", alpha=1, label="driver with fixed obey rate")
    
    plt.legend()
    
    plt.savefig("p_pu.pdf")
    plt.show()
