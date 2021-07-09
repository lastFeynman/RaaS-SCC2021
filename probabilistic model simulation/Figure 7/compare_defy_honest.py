import matplotlib.pyplot as plt

honest_x = []
honest_y = []

fixed_x = []
fixed_y = []

adjusted_x = []
adjusted_y = []

adjusted_x_r_2 = []
adjusted_y_r_2 = []

adjusted_x_r_3 = []
adjusted_y_r_3 = []

adjusted_x_r_4 = []
adjusted_y_r_4 = []

adjusted_x_r_5 = []
adjusted_y_r_5 = []


def read_bak_file(filename, x, y):
    with open(filename, 'r') as f:
        for i in range(1000):
            x.append(i+1)
            y.append(float(f.readline()))
        f.close()


if __name__ == "__main__":
    plt.figure(figsize=(9, 6))
    font = {'family': 'normal',
           'size': 14}

    plt.rc('font', **font)

    read_bak_file("honest", honest_x, honest_y)
    read_bak_file("fixed_obey", fixed_x, fixed_y)
    read_bak_file("adjusted_obey", adjusted_x, adjusted_y)
    read_bak_file("adjusted_obey_r_2", adjusted_x_r_2, adjusted_y_r_2)
    read_bak_file("adjusted_obey_r_3", adjusted_x_r_3, adjusted_y_r_3)
    read_bak_file("adjusted_obey_r_4", adjusted_x_r_4, adjusted_y_r_4)
    read_bak_file("adjusted_obey_r_5", adjusted_x_r_5, adjusted_y_r_5)

    plt.xlabel("Driver Number")
    plt.ylabel("Total Incomes")


    plt.plot(adjusted_x_r_4, adjusted_y_r_4, color="purple", alpha=0.7, label="driver profile $\\xi$ = 0.1")
    # plt.plot(adjusted_x_r_3, adjusted_y_r_3, color="black", alpha=0.7, label="driver profile r = 0.5")
    # plt.plot(adjusted_x_r_5, adjusted_y_r_5, color="orange", alpha=0.7, label="driver profile r = 0.7")
    plt.plot(adjusted_x, adjusted_y, color="blue", alpha=0.7, label="driver profile $\\xi$ = 1")
    plt.plot(adjusted_x_r_2, adjusted_y_r_2, color="orange", alpha=0.7, label="driver profile $\\xi$ = 2")
    plt.plot(fixed_x, fixed_y, color="red", alpha=0.7, label="driver with fixed obey rate")
    plt.plot(honest_x, honest_y, color="green", alpha=1, label="disciplined driver")

    plt.legend(ncol=2, bbox_to_anchor=(0.52, 0.5, 0.4, -0.65))
    plt.tight_layout()
    plt.savefig("compare.pdf")
    plt.show()

    fixed_above_count = 0
    adjusted_above_count = 0
    adjusted_r_2_above_count = 0
    adjusted_r_3_above_count = 0
    adjusted_r_4_above_count = 0
    adjusted_r_5_above_count = 0

    for i in range(1000):
        if fixed_y[i] > honest_y[i]:
            fixed_above_count += 1
        if adjusted_y[i] > honest_y[i]:
            adjusted_above_count += 1
        if adjusted_y_r_2[i] > honest_y[i]:
            adjusted_r_2_above_count += 1
        if adjusted_y_r_3[i] > honest_y[i]:
            adjusted_r_3_above_count += 1
        if adjusted_y_r_4[i] > honest_y[i]:
            adjusted_r_4_above_count += 1
        if adjusted_y_r_5[i] > honest_y[i]:
            adjusted_r_5_above_count += 1

    print("fixed possibility:" + str(fixed_above_count/1000))
    print("adjusted possibility:" + str(adjusted_above_count/1000))
    print("adjusted r=2 possibility:" + str(adjusted_r_2_above_count/1000))
    print("adjusted r=0.5 possibility:" + str(adjusted_r_3_above_count/1000))
    print("adjusted r=0.1 possibility:" + str(adjusted_r_4_above_count/1000))
    print("adjusted r=0.7 possibility:" + str(adjusted_r_5_above_count/1000))