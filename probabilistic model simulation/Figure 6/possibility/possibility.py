import matplotlib.pyplot as plt
import os

def punish():
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

    read_files("pu/possibility",
               fixed_y,
               adjust_r_01_y,
               adjust_r_05_y,
               adjust_r_07_y,
               adjust_r_1_y,
               adjust_r_2_y)

    plt.xlabel("$k_{punish}$\n(b) Different $k_{punish}$ and fixed $K_{reward}$")
    plt.ylabel("Probability")

    plt.plot(adjust_r_01_x, adjust_r_01_y, color="red", alpha=1, label="driver profile $\\xi$ = 0.1")
    plt.plot(adjust_r_05_x, adjust_r_05_y, color="brown", alpha=1, label="driver profile $\\xi$ = 0.5")
    plt.plot(adjust_r_07_x, adjust_r_07_y, color="purple", alpha=1, label="driver profile $\\xi$ = 0.7")
    plt.plot(adjust_r_1_x, adjust_r_1_y, color="grey", alpha=1, label="driver profile $\\xi$ = 1")
    plt.plot(adjust_r_2_x, adjust_r_2_y, color="orange", alpha=1, label="driver profile $\\xi$ = 2")
    plt.plot(fixed_x, fixed_y, color="green", alpha=1, label="driver with fixed obey rate")

    plt.legend(bbox_to_anchor=(0.4, 0.3, 0.4, 0.6))

def reward():
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

    read_files("re/possibility",
               fixed_y,
               adjust_r_01_y,
               adjust_r_05_y,
               adjust_r_07_y,
               adjust_r_1_y,
               adjust_r_2_y)

    plt.xlabel("$k_{reward}$\n(a) Different $k_{reward}$ and fixed $K_{punish}$")
    plt.ylabel("Probability")

    plt.plot(adjust_r_01_x, adjust_r_01_y, color="red", alpha=1, label="driver profile $\\xi$ = 0.1")
    plt.plot(adjust_r_05_x, adjust_r_05_y, color="brown", alpha=1, label="driver profile $\\xi$ = 0.5")
    plt.plot(adjust_r_07_x, adjust_r_07_y, color="purple", alpha=1, label="driver profile $\\xi$ = 0.7")
    plt.plot(adjust_r_1_x, adjust_r_1_y, color="grey", alpha=1, label="driver profile $\\xi$ = 1")
    plt.plot(adjust_r_2_x, adjust_r_2_y, color="orange", alpha=1, label="driver profile $\\xi$ = 2")
    plt.plot(adjust_r_2_x, adjust_r_2_y, color="orange", alpha=1, label="driver profile $\\xi$ = 2")
    plt.plot(fixed_x, fixed_y, color="green", alpha=1, label="driver with fixed obey rate")

    plt.legend()

def read_files(path, v1, v2, v3, v4, v5, v6):
    with open(path) as f:
        x = 0
        while x != "[":
            x = f.read(1)
            continue;
        x = f.readline()[:-2]
        ps = x.split(", ")
        for p in ps:
            v1.append(float(p))

        x = 0
        while x != "[":
            x = f.read(1)
            continue;
        x = f.readline()[:-2]
        ps = x.split(", ")
        for p in ps:
            v2.append(float(p))

        x = 0
        while x != "[":
            x = f.read(1)
            continue;
        x = f.readline()[:-2]
        ps = x.split(", ")
        for p in ps:
            v3.append(float(p))

        x = 0
        while x != "[":
            x = f.read(1)
            continue;
        x = f.readline()[:-2]
        ps = x.split(", ")
        for p in ps:
            v4.append(float(p))

        x = 0
        while x != "[":
            x = f.read(1)
            continue;
        x = f.readline()[:-2]
        ps = x.split(", ")
        for p in ps:
            v5.append(float(p))

        x = 0
        while x != "[":
            x = f.read(1)
            continue;
        x = f.readline()[:-2]
        ps = x.split(", ")
        for p in ps:
            v6.append(float(p))


if __name__ == "__main__":
    plt.figure(figsize=(6, 7))


    plt.subplot(2, 1, 1)
    reward()

    plt.subplot(2, 1, 2)
    punish()

    plt.tight_layout()

    plt.savefig("possibility.pdf")
    plt.show()


